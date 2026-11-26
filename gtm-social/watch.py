"""Plan public social research runs and archive sourced research results."""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import parse_qsl, urlsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
WATCHLISTS = ROOT / "watchlists"
OUTPUT = ROOT.parent / "output" / "gtm-social"
STATUSES = {"observed", "partial", "no_matches", "restricted"}
MODES = {"organic", "paid", "platform", "unknown"}
METRICS = {"views", "impressions", "reactions", "likes", "comments", "reposts", "votes"}
SINGULAR = {"views": "view", "impressions": "impression", "reactions": "reaction",
            "likes": "like", "comments": "comment", "reposts": "repost", "votes": "vote"}


def read_json(file):
    return json.loads(file.read_text(encoding="utf-8-sig"))


def load_watchlist(key):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key):
        raise ValueError("Use a lowercase watchlist ID with hyphens.")
    config = read_json(WATCHLISTS / f"{key}.json")
    for field in ("name", "market", "goal"):
        if not isinstance(config[field], str) or not config[field].strip():
            raise ValueError(f"{key}: {field} must be nonempty text.")
    if not config["topics"] or not config["sources"]:
        raise ValueError(f"{key}: provide topics and at least one source.")
    for field in ("topics", "accounts", "exclude"):
        if not isinstance(config[field], list) or any(not isinstance(item, str) for item in config[field]):
            raise ValueError(f"{key}: {field} must be a list of text values.")
    for platform, source in config["sources"].items():
        if not platform or not source["method"] or not isinstance(source["hosts"], list) or not source["hosts"]:
            raise ValueError(f"{key}: each platform must have hosts and a research method.")
    days = config["lookback_days"]
    if type(days) is not int or not 1 <= days <= 366:
        raise ValueError(f"{key}: lookback_days must be 1 to 366.")
    return config


def schedule_slot(schedule, now):
    """Latest elapsed slot only. Day/week schedules preserve local wall time."""
    if schedule is None:
        return None
    if type(schedule["enabled"]) is not bool:
        raise ValueError("Schedule enabled must be true or false.")
    every = schedule["every"]
    unit = schedule["unit"]
    if type(every) is not int or every < 1 or unit not in {"hours", "days", "weeks"}:
        raise ValueError("Use a positive schedule interval in hours, days or weeks.")
    zone = ZoneInfo(schedule["time_zone"])
    start = datetime.fromisoformat(schedule["start_local"])
    if start.tzinfo is not None:
        raise ValueError("Specify start_local without an offset and give time_zone separately.")
    if not schedule["enabled"]:
        return None
    if unit == "hours":
        start = start.replace(tzinfo=zone).astimezone(timezone.utc)
        current = now.astimezone(timezone.utc)
    else:
        current = now.astimezone(zone).replace(tzinfo=None)
    if current < start:
        return None
    step = timedelta(**{unit: every})
    position = (current - start) // step
    slot = start + position * step
    resolved = slot.replace(tzinfo=slot.tzinfo or zone).astimezone(timezone.utc)
    if resolved <= now:
        return resolved
    if position == 0:
        return None
    return (slot - step).replace(tzinfo=slot.tzinfo or zone).astimezone(timezone.utc)


def make_plan(key, config, anchor, run_id):
    start = anchor - timedelta(days=config["lookback_days"] - 1)
    previous_start = start - timedelta(days=config["lookback_days"])
    folder = OUTPUT / key
    previous = next(iter(sorted(folder.glob("*.json"), key=lambda p: p.name[2:], reverse=True)), None)
    return {
        "watchlist": key, "run_id": run_id,
        "current": [start.isoformat(), anchor.isoformat()],
        "previous": [previous_start.isoformat(), (start - timedelta(days=1)).isoformat()],
        "latest_saved": str(previous) if previous else None,
        "config": config,
    }


def scheduled_plans(now):
    pending = []
    for file in sorted(WATCHLISTS.glob("*.json")):
        try:
            config = load_watchlist(file.stem)
            slot = schedule_slot(config["schedule"], now)
            if slot:
                run_id = slot.strftime("s-%Y%m%dT%H%M%SZ")
                if not (OUTPUT / file.stem / f"{run_id}.json").exists():
                    local_day = slot.astimezone(ZoneInfo(config["schedule"]["time_zone"])).date()
                    pending.append(make_plan(file.stem, config, local_day, run_id))
        except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
            print(f"{file.name}: {exc}", file=sys.stderr)
    return pending


def host_matches(url, domains):
    parsed = urlsplit(url)
    name = parsed.hostname or ""
    return (parsed.scheme == "https" and not parsed.username and not parsed.password
            and not re.search(r"[\s<>]", url)
            and any(name == domain or name.endswith("." + domain) for domain in domains))


def validate(plan, payload):
    sources = plan["config"]["sources"]
    coverage = payload["coverage"]
    if set(coverage) != set(sources):
        raise ValueError("Provide coverage for every configured platform.")
    for platform, entry in coverage.items():
        if entry["status"] not in STATUSES or type(entry["comparable"]) is not bool or not entry["detail"].strip():
            raise ValueError(f"Invalid coverage record for {platform}.")
        if entry["comparable"] and entry["status"] not in {"observed", "no_matches"}:
            raise ValueError(f"Partial or restricted evidence cannot be marked comparable for {platform}.")
    seen = set()
    for item in payload["observations"]:
        platform = item["platform"]
        url = item["url"]
        if not host_matches(url, sources[platform]["hosts"]):
            raise ValueError(f"Use an HTTPS permalink on a configured host for {platform}.")
        parsed = urlsplit(url)
        domain = next(domain for domain in sources[platform]["hosts"] if
                      parsed.hostname == domain or parsed.hostname.endswith("." + domain))
        post_identifiers = {"v", "story_fbid", "fbid", "id"}
        identity = (platform, domain, parsed.path.rstrip("/"),
                    tuple(sorted(pair for pair in parse_qsl(parsed.query) if pair[0] in post_identifiers)))
        if identity in seen:
            raise ValueError(f"Duplicate observation {url}")
        seen.add(identity)
        if item["mode"] not in MODES:
            raise ValueError(f"Unknown content mode for {url}")
        for field in ("publisher", "theme", "summary", "format"):
            if not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"Observation missing {field}.")
        if item["published"]:
            published = date.fromisoformat(item["published"])
            if published > date.fromisoformat(plan["current"][1]):
                raise ValueError(f"Publication date is after the report window for {url}.")
        metrics = item["metrics"]
        if set(metrics) - METRICS or any(type(value) is not int or value < 0 for value in metrics.values()):
            raise ValueError("Record exact visible counts or omit the metric.")
        if metrics:
            date.fromisoformat(item["metrics_as_of"])
    for action in payload["tests"]:
        if not action["idea"].strip() or not action["success_metric"].strip():
            raise ValueError("Each test needs an idea and success metric.")
        urls = {item["url"] for item in payload["observations"]}
        if not action["evidence"] or any(url not in urls for url in action["evidence"]):
            raise ValueError("Link each test to at least one observation.")


def sample_trends(plan, payload):
    """Compare distinct publishers in two equivalent, dated organic samples."""
    current_start, current_end = plan["current"]
    previous_start, previous_end = plan["previous"]
    buckets = {}
    for item in payload["observations"]:
        source = payload["coverage"][item["platform"]]
        published = item["published"]
        if not (source["comparable"] and published and item["mode"] == "organic"):
            continue
        if current_start <= published <= current_end:
            index = 1
        elif previous_start <= published <= previous_end:
            index = 0
        else:
            continue
        key = (item["platform"], item["theme"].casefold())
        samples = buckets.setdefault(key, [set(), set(), []])
        samples[index].add(item["publisher"].strip().casefold())
        if index == 1:
            samples[2].append(item["url"])
    for (platform, theme), (earlier, latest, urls) in sorted(buckets.items()):
        if len(latest) >= 3 and len(latest) >= len(earlier) + 2:
            yield platform, theme, len(earlier), len(latest), urls


def text(value):
    return " ".join(value.split()).replace("[", "\\[").replace("]", "\\]")


def build_report(plan, payload):
    start, end = plan["current"]
    previous_start, previous_end = plan["previous"]
    lines = [f"# {text(plan['config']['name'])}", "", f"Research window **{start} to {end}**. {text(plan['config']['market'])}",
             "", "## What people are posting", ""]
    for item in payload["observations"]:
        date_label = item["published"] or "publication date unverified"
        if item["published"] and item["published"] < start:
            date_label += ", outside current window"
        evidence = f"[Source](<{item['url']}>)"
        lines.append(f"- **{text(item['publisher'])} · {text(item['platform'])}** ({item['mode']}, {text(item['format'])}, {date_label}). {text(item['summary'])} {evidence}")
    if not payload["observations"]:
        lines.append("No relevant source-backed examples were recorded.")
    lines += ["", "## Visible performance", ""]
    for item in payload["observations"]:
        if item["metrics"]:
            counts = ", ".join(f"{value:,} {SINGULAR[metric] if value == 1 else metric}"
                               for metric, value in item["metrics"].items())
            context = text(item.get("metrics_context", ""))
            note = f" {context}" if context else ""
            lines.append(f"- {text(item['platform'])} · {text(item['publisher'])} · {counts} recorded on {item['metrics_as_of']}.{note} [Source](<{item['url']}>)")
    lines += ["", text(payload["performance_read"]), "", "## Topic momentum",
              "", f"Comparison window **{previous_start} to {previous_end}**.", ""]
    lines += [f"- **{text(theme)} · {text(platform)}** appeared from {after} distinct publishers in the current covered sample and {before} in the previous sample. "
              + " ".join(f"[Example {i}](<{url}>)" for i, url in enumerate(urls[:5], 1))
              for platform, theme, before, after, urls in sample_trends(plan, payload)]
    if lines[-1] == "":
        lines.append("No topic met the evidence threshold for rising activity in a comparable public sample.")
    lines += ["", "## Tests for Skarion", ""]
    for action in payload["tests"]:
        citations = " ".join(f"[Evidence {i}](<{url}>)" for i, url in enumerate(action["evidence"], 1))
        lines.append(f"- **{text(action['idea'])}**. Measure {text(action['success_metric'])}. {citations}")
    lines += ["", "## Platform coverage", ""]
    for platform, entry in payload["coverage"].items():
        status = entry["status"].replace("_", " ")
        lines.append(f"- **{text(platform)} · {status}**. {text(entry['detail'])}")
    return "\n".join(lines) + "\n"


def atomic_write(path, content, *, exclusive=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as temp:
        temp.write(content)
        temp_path = Path(temp.name)
    try:
        if not exclusive:
            temp_path.replace(path)
        elif os.name == "nt":
            temp_path.rename(path)
        else:
            os.link(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)


def record(plan, payload):
    key, run_id = plan["watchlist"], plan["run_id"]
    config = load_watchlist(key)
    if not re.fullmatch(r"[ms]-\d{8}T\d{6}Z", run_id):
        raise ValueError("Run ID must come from the watchlist planner.")
    clean_plan = make_plan(key, config, date.fromisoformat(plan["current"][1]), run_id)
    if clean_plan["current"] != plan["current"] or clean_plan["previous"] != plan["previous"] or config != plan["config"]:
        raise ValueError("Watchlist or windows changed. Regenerate the research plan.")
    destination = OUTPUT / key / run_id
    snapshot = destination.with_suffix(".json")
    report = destination.with_suffix(".md")
    if not snapshot.exists():
        validate(clean_plan, payload)
        content = json.dumps({"plan": clean_plan, "payload": payload}, ensure_ascii=False, indent=2) + "\n"
        try:
            atomic_write(snapshot, content, exclusive=True)
        except FileExistsError:
            pass
    saved = read_json(snapshot)
    if not report.exists():
        atomic_write(report, build_report(saved["plan"], saved["payload"]))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    due = commands.add_parser("due", help="Show due runs for enabled watchlists")
    due.add_argument("--at", help="Override the clock with an aware ISO timestamp")
    manual = commands.add_parser("now", help="Plan an on-demand run")
    manual.add_argument("watchlist")
    manual.add_argument("--end", type=date.fromisoformat, help="Report through this date")
    save = commands.add_parser("record", help="Validate and save post observations and a digest")
    save.add_argument("plan", type=Path)
    save.add_argument("observations", type=Path)
    args = parser.parse_args()
    try:
        now = datetime.now(timezone.utc)
        if args.command == "due":
            now = datetime.fromisoformat(args.at) if args.at else now
            if now.tzinfo is None:
                raise ValueError("--at must contain a time-zone offset.")
            result = scheduled_plans(now)
        elif args.command == "now":
            anchor = args.end or datetime.now().astimezone().date()
            result = make_plan(args.watchlist, load_watchlist(args.watchlist),
                               anchor, now.strftime("m-%Y%m%dT%H%M%SZ"))
        else:
            print(record(read_json(args.plan), read_json(args.observations)))
            return 0
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
        print(exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
