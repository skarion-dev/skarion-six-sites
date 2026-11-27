# VCL AI Agents Project: Full Context Handoff

Use this file to continue the work in a new chat. It covers the project, the supervisor's feedback, the decisions made so far, every file created, and the open items.

---

## 1. Who and what

- **User:** Avirup Bhattacharjee, VCL (lighting and electrical design firm, Southern California). Works in AutoCAD on electrical and lighting drawings. Owns the VCL AI agents planning effort.
- **Project:** Plan, prioritize and build AI agents ("helpers") in **Microsoft Copilot** to take repetitive checking and paperwork off the design team.
- **Existing agent:** **Reviewer Rachel**, a QC/review agent built by VCL's most experienced lighting designer. It's already in use.
- **Coworkers to survey:**
  - **Kam**: most experienced in electrical design. Gets the Electrical form. (Possibly Kameron Burns, a top collaborator. Not confirmed, and his email address wasn't found.)
  - **Lighting design lead**: most experienced in lighting design and the builder of Reviewer Rachel. Gets the Lighting + Rachel form. (Name not given in chat.)
- **User preferences:** plain, simple wording; uncluttered documents; practical step-by-step guidance; precise answers.

---

## 2. Original plan (source document)

**File:** `VCL-AI-Helpers-Plan.pdf`, titled "Our Plan for 10 AI Helpers at VCL", dated Nov 2, 2026, by Avirup. 6 pages.

**Core idea:** Each helper reads incoming files using VCL's rulebook (skill files: standards, city codes, past comments) and drafts a checklist, letter or calculation. A VCL team member approves it, and nothing goes out without sign-off. Lessons learned feed back into the rulebook.

**Project workflow and the original 10 helpers:**

| Project step | Helpers |
|---|---|
| 1. Consultant drawings arrive | 1 File Intake |
| 2. Clean up and combine bases | 2 Mbase & Revision Tracker, 3 CAD Cleanup |
| 3. Design the lighting | 4 Code & Ordinance Research, 5 Photometric Check, 6 Electrical Calculations |
| 4. Quality review | Reviewer Rachel (in use), 7 Cross-Check |
| 5. Submit for permit | 8 Permit Submittal |
| 6. City comments, then approval | 9 Plan Check Response |
| Across every project | 10 Cost Estimator |

**Original rollout:**
- Step 1 (quick wins): helpers 9, 4, 10, 1
- Step 2 (AutoCAD link): helpers 3, 2, 7
- Step 3 (design support): helpers 5, 6, 8

**Safeguards:**
- People make the decisions.
- Nothing goes out without sign-off.
- Stamped work stays with the engineer of record.
- Files stay in VCL's Microsoft 365.

**Page 6 checklist:**
- Go-ahead to build the first 4 helpers
- Shared SharePoint folder for the rulebooks
- Past plan-check letters, fee history and city codes
- 1–2 live projects for testing

**Issues from my earlier reviews:**
- Some claims go too far: "one click" CAD Cleanup, Photometric "confirms" results, and helpers that "get better" by themselves (someone has to update the rulebook).
- Calculations should come from fixed calculators or software, with the AI only comparing results and explaining them.
- Every code requirement needs a source link and a "checked as of" date.
- Cost Estimator isn't a quick win, because it needs clean historical data.
- Missing: an owner, a timeline, success measures, cost and licensing, who builds the CAD link, and an introduction to Rachel.
- Layout: the "Photo to add" placeholder is still on page 4, and the helper table breaks badly across pages.

---

## 3. Supervisor's markups (key direction)

| Markup | Meaning |
|---|---|
| Steps 1–3 highlighted | Focus on the front half of the workflow |
| **#1 priority:** "determine number of agents required" (Code Research, Photometric, Electrical) | Decide how many design agents are needed |
| **#2 priority:** Reviewer Rachel + Cross-Check | QC comes next |
| **#3 priority:** Cost Estimator ("Project estimator") | Estimating comes third |
| Permit Submittal crossed out | **Removed.** Permits are the client's responsibility, and VCL doesn't offer this service |
| Plan Check: "agent to confirm plan check comments have been addressed" | Becomes **Plan Check Verification** |
| "2 agents on the front end" | **Add** a Marketing Agent (finds project leads, fits business strategy) and a Proposal Estimator (fee structure, competitive bids) |
| "AI integration into company operations" | Present this as a company-wide effort |
| "Integration with Outlook, email forwarding to team" | Applies to File Intake and Revision Tracker |
| "Permissions?" | Define who can use each agent and what data it can see |
| Page 6 checklist items 1–3 = "Phase 1"; live projects = "Phase 2 Pilot test/integration" | Restructure the rollout into these phases |
| "How to create an Agent through Co-pilot" | Add a how-to section |

**Inconsistency to ask him about:** On page 2, Cost Estimator is #3. On the rollout diagram, the Step 1 / Cost Estimator area is marked #2 and Step 2 (CAD) is marked #3.

---

## 4. Current game plan (agreed direction)

**Stage now:** Phase 0, Discovery. The plan has been revised and both forms are ready or being sent. No new agents have been built yet.

| Phase | Focus |
|---|---|
| 0 Discovery | Questionnaires, follow-up chats, document how Rachel was built, decide the number of design agents |
| 1 Setup | SharePoint knowledge base, permissions, agent build guide |
| 2 Pilot: Design agents (#1) | Build and test on 1–2 live projects |
| 3 QC (#2) | Cross-Check with Rachel, Plan Check Verification |
| 4 Estimating (#3) | Project/Cost Estimator, Proposal Estimator |
| 5 Operations | File Intake and Revision Tracker (Outlook), CAD Cleanup and Mbase link (needs AutoCAD scripting), Marketing Agent |

**Design agent recommendation:** start with **two agents**, to be confirmed by the questionnaire answers.

- **Lighting Design agent:**
  - City code summary, with a source and "checked as of" date for each requirement
  - Compares exported photometric results to city limits and flags gaps
  - Drafts the summary table
  - Checks the fixture schedule
- **Electrical Design agent:**
  - Checks results from VCL's calc spreadsheet against VCL's rules
  - Flags circuits that need review
  - Checks that plans and schedules match

The alternatives were one combined agent or three separate agents.

**Rule:** The agents only check and flag. Software does the math, and designers and the engineer of record decide.

**How to build each agent:**
1. Gather files in SharePoint.
2. Write the instructions: role, inputs, steps, rules, output format, and what it must never do.
3. Build it with Copilot's "Create agent" (Agent Builder), or Copilot Studio for advanced needs like Outlook triggers (IT may need to confirm licensing).
4. Test it on 3–5 finished projects.
5. Pilot it on 1–2 live projects.
6. Assign an owner to maintain it.

**Questions still open for the supervisor:**
1. Confirm the priority order.
2. Should the Proposal Estimator replace the Cost Estimator, or do we keep both?
3. Does "Permissions" mean who can use each agent, what data it sees, or both?
4. Can Phase 1 setup start now?

---

## 5. Questionnaires / Microsoft Forms

**Purpose:** Understand each lead's day-to-day process, how much they use AI and how much it has helped, which tasks are repetitive, and their ideas for agents. Answers are built to be chartable (KPIs, stats). Rachel's build process and accuracy are covered in depth.

**Format:**
- Choice questions: multiple answers ON plus an "Other" write-in, for lists
- Single-answer questions for numbers to chart: hours per task, frequency, %, years
- Ranking (drag to order)
- Rating (1–5)
- Likert grid (how repetitive each task is)
- A few long-text questions

**Intro text (in each form):**
- Why they're receiving it
- What it's for and what sections it covers
- How answers are used: only to plan the agents; not a performance review
- How to answer each question type
- About 25–35 minutes; progress isn't saved, so finish in one sitting
- Deadline **[date]**, still to fill in

**Electrical form (45 questions), sections:**
1. About you
2. Your day-to-day process (hours per task: load calcs, voltage drop and conductor sizing, circuiting and schedules, notes and details, utility coordination, plan check)
3. Calculations and standards (whether rules are written down, thresholds, redo frequency, costly errors)
4. Drawings, QC and plan check
5. AI tools today
6. Repetitive tasks and agent ideas
7. Working with an agent (output format, inputs, never-do, permissions, pilot willingness)
8. Final thoughts

**Lighting + Rachel form (62 questions), sections:**
1. About you
2. Your day-to-day process (hours for code research, fixture selection, calc grids, summary table, schedule coordination, plan check)
3. Code research and photometrics
4. **Rachel: how you built it** (problem, tool, step-by-step build, time, help used)
5. **Rachel: skills and knowledge** (instructions text, knowledge sources, checklist origin, how skills were added, maintenance)
6. **Rachel: how it works today** (usage steps, number of users, reviews per month, file type handling)
7. **Rachel: accuracy and results** (% of real flags, % missed, testing method, what it catches or misses, time saved, satisfaction, lessons)
8. AI tools today, repetitive tasks and agent ideas, working with an agent, final thoughts

**How to build the forms in Microsoft Forms:**
1. Go to the forms.office.com **home page**. Quick import is NOT inside a blank form's editor. It's next to New Form, or in the New Form dropdown.
2. Choose Quick import, upload the Word file and select **Form**.
3. Fix the question types using the Excel build key.
4. For lists, turn on **Multiple answers**, then click **Add "Other" option**. If the import brought "Other" in as a plain choice, delete it and re-add it this way.
5. Settings: only people in my organization can respond; Record name ON.
6. Collect responses, then Copy link, and share.
7. To get results: Responses tab, then Open in Excel.

**Fallbacks:**
- Try "Quick start with" in the editor.
- Or use "Draft with Copilot", paste one section at a time, then fix the question types.

**Limitation:** Copilot couldn't create the live forms or links directly. The user builds them.

---

## 6. Email to Kam (drafted)

**Subject:** Your input on VCL's AI design agents – short form (25–35 min)

The email covers:
- The purpose: Copilot agents like Rachel, with design agents first
- What the form covers
- That it's mostly click, select, rank and rate, with "Other" for adding answers and only a few typed answers
- Notes: 25–35 minutes in one sitting, estimates are fine, not a performance review, "show me" option
- Deadline [date]
- Follow-up before any electrical agent is built

**To fill in before sending:** the form link, the date and Kam's email address.

---

## 7. Files created in this chat (in Avirup's OneDrive)

| File | What it is | Status |
|---|---|---|
| `VCL-AI-Helpers-Plan.pdf` | Original 10-helper plan (source) | Superseded by the revised plan |
| `VCL_AI_Agents_Gameplan.docx` | First revised game plan (design first, phases, options, guardrails, metrics) | Older version |
| `Questionnaire_Electrical_Design_Lead.docx` | First written questionnaire, electrical (about 45 questions) | Replaced by forms |
| `Questionnaire_Lighting_Design_Lead_Reviewer_Rachel.docx` | First written questionnaire, lighting + Rachel (about 65 questions) | Replaced by forms |
| `Form_Import_Electrical_Design.docx` / `Form_Import_Lighting_Design_Rachel.docx` / `Form_Build_Key_Question_Types.xlsx` | First Forms import files and build key | Replaced by v2 |
| **`Form_Import_Electrical_Design_v2.docx`** | Forms import file, electrical, 45 questions with full intro | **Current** |
| **`Form_Import_Lighting_Design_Rachel_v2.docx`** | Forms import file, lighting + Rachel, 62 questions with full intro | **Current** |
| **`Form_Build_Key_v2.xlsx`** | One tab per form listing question, type, options, "Other" ON (green) and required | **Current** |
| `VCL_AI_Agents_Next_Steps_Report.docx` | Detailed 11-section supervisor report | Detailed backup |
| **`VCL_AI_Agents_Next_Steps.pdf`** | Clean 2-page report in plain words (summary, status, priorities, design agents, 6 build steps, benefits, next steps, questions) | **Current, for the supervisor** |

---

## 8. Open to-dos

- [ ] Build both forms in Microsoft Forms, fill in [date] and copy the links
- [ ] Send the Electrical form to Kam (add his email) and the Lighting form to the lighting lead
- [ ] Present `VCL_AI_Agents_Next_Steps.pdf` to the supervisor and get answers to the 4 open questions
- [ ] Start Phase 1: SharePoint "VCL AI Knowledge Base" folders (Lighting Standards, Electrical Standards, City Codes, Calc Templates, Past Plan Check Letters, Rachel Lessons)
- [ ] When responses arrive: export to Excel, then build KPI charts (hours per task, repetitiveness, rankings, trust/satisfaction ratings, Rachel accuracy)
- [ ] Follow-up chats and screen-shares, including a walkthrough of how Rachel was built
- [ ] Recommend the final number of design agents, then build the first agent and test it on past projects
- [ ] Fix the original plan's layout issues (photo placeholder, table break) if it's reused
