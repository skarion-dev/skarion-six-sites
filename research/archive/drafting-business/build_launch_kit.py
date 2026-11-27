from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / 'output' / 'pdf'
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'Skarion_Drafting_Launch_Playbook.pdf'
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleA', fontName='Helvetica-Bold', fontSize=26, leading=30, spaceAfter=14, textColor=colors.black))
styles.add(ParagraphStyle(name='Deck', fontName='Helvetica', fontSize=12, leading=17, spaceAfter=14, textColor=colors.HexColor('#334155')))
styles.add(ParagraphStyle(name='SectionA', fontName='Helvetica-Bold', fontSize=19, leading=23, spaceAfter=12, textColor=colors.black))
styles.add(ParagraphStyle(name='SubA', fontName='Helvetica-Bold', fontSize=11.5, leading=15, spaceBefore=8, spaceAfter=4, keepWithNext=True, textColor=colors.black))
styles.add(ParagraphStyle(name='BodyA', fontName='Helvetica', fontSize=10.5, leading=14, spaceAfter=6))
styles.add(ParagraphStyle(name='SmallA', fontName='Helvetica', fontSize=8.7, leading=11.6, spaceAfter=6, textColor=colors.HexColor('#475569')))
styles.add(ParagraphStyle(name='CellA', fontName='Helvetica', fontSize=9.5, leading=12.7, spaceAfter=0))
styles.add(ParagraphStyle(name='HeadCell', fontName='Helvetica-Bold', fontSize=9.5, leading=12.7, textColor=colors.white))
story=[]

def p(text, style='BodyA'):
    story.append(Paragraph(text, styles[style]))

def sub(title): p(title,'SubA')

def bullets(items):
    for item in items:
        p('• ' + item)

def table(headers, rows, widths):
    cells=[[Paragraph(escape(str(c)),styles['HeadCell']) for c in headers]]
    cells += [[Paragraph(escape(str(c)),styles['CellA']) for c in row] for row in rows]
    t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#193549')),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F2F5F7')]),
        ('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#D9D9D9')),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
    ]))
    story.append(t); story.append(Spacer(1,8))

def page(title):
    story.append(PageBreak()); p(title,'SectionA')

def source(title,url):
    p(f'<link href="{escape(url)}" color="#1E587D">{escape(title)}</link>', 'SmallA')

p('Skarion Drafting<br/>Launch Playbook','TitleA')
p('A practical plan to win the first recurring CAD production clients','Deck')
p('Prepared November 12, 2026 | Planning period November 13 to December 12, 2026','SmallA')
p('<b>Launch a small CAD production service for US architecture and interior-design firms.</b> Start with controlled drawing revisions and conversion of clear source drawings. Use paid pilots to demonstrate the team\'s work, then sell scheduled blocks of production hours.')
p('The owner has confirmed that an experienced architectural drafter is available, the working brand is Skarion Drafting, and the first 30 days must cost less than $1,000 in additional cash, excluding existing salaries. The plan sets a $950 ceiling. These are planning allocations, not purchases or commitments.')
sub('What success means after 30 days')
table(['Outcome','Target','Evidence'],[
('Delivery readiness','3 reviewed sample exercises','DWG, plotted PDF, source comparison and issue log'),
('Commercial validation','2 paid pilots delivered','Accepted scope, payment record, time and cost record'),
('Repeat demand','1 repeat order or 20 hour block','A funded order; a discussion alone is not revenue'),
('Sales learning','30 qualified firms and up to 10 targeted bids','Verified contacts, actual responses and reasons lost'),
('Economics','At least 40% pilot contribution','After direct labor, review, PM, rework and transaction fees'),
], [112,150,242])
sub('The operating decision')
p('Allocate a small, measured portion of the existing drafter\'s time. Add an independent reviewer for initial samples and deliveries. Keep one accountable sales and project coordinator. Increase capacity only after repeat orders demonstrate that the price covers the actual work.')
sub('Decisions to settle before taking the first order')
bullets([
'Name the drafter, reviewer and coordinator; verify weekly availability against existing Skarion commitments.',
'Confirm a commercial CAD license, client-compatible DWG version and a secure file-sharing method.',
'Confirm the contracting entity, target project jurisdictions and permitted service wording. The working brand has not been cleared for trademark or business-name use.',
])

page('The first offers and prices')
p('Sell a small, clearly defined production task first. The following prices are proposed tests, not market averages. Confirm source quality and estimated hours before quoting.')
table(['Offer','Proposed price','Scope'],[
('Paid production pilot','$175 to $350 fixed','One small drawing package from complete client inputs. Layered DWG, plotted PDF, assumptions log and one consolidated review round.'),
('Scheduled production support','$640 for 20 production hours','Use over 30 days, scheduled at about 5 hours per week. Routine internal review included. Client changes consume hours; corrections to Skarion errors do not.'),
('Additional production hours','$32 to $38 per hour','Written estimate and client approval before overage. Rate depends on complexity, source quality and service requirements.'),
], [114,115,275])
sub('A defined starting pilot')
p('Offer the $175 pilot only when the source supports about 4 production hours, 1 review hour, 0.5 project-coordination hour and a 1 hour drafting rework allowance. Suitable work includes a straightforward floor-plan conversion or a contained redline revision. A sheet count alone does not establish complexity.')
p('The $350 package may cover about 8 production hours, 1.5 review hours, 1 coordination hour and 1.5 drafting rework hours. Re-estimate when inputs are incomplete, the drawing is dense, or client standards require substantial setup.')
sub('Delivery terms to put in every quote')
bullets([
'List exact sheets, views, source filenames and revisions, required layers, units, DWG version, plot size, deliverables and exclusions.',
'For a small qualified pilot, propose a first draft in 3 business days after complete inputs, agreed scope and payment setup. Confirm the actual date before accepting.',
'Include one consolidated review round within 5 business days. Correct Skarion transcription errors without consuming the client\'s change allowance; price new design decisions or new source material separately.',
'For direct pilots, propose 50% to start and 50% on acceptance before final editable-file release. On Upwork, use funded milestones and its delivery/payment workflow.',
'Define the monthly block as scheduled production capacity, not unlimited work. Agree expiry, rollover and refund rules in writing; unused hours and an unbooked discussion are not recognized revenue.',
])
sub('Scope for the first month')
p('Accept redline incorporation, layered PDF/sketch-to-DWG conversion and updates based on client-verified measurements. Describe the latter as drawings prepared from supplied records. Field-verified as-built services require separate measurement evidence and scope. Defer independent design, engineering calculations, permit responsibility, fabrication detailing and BIM until the appropriate capability and project requirements are established.')

page('How each job reaches delivery')
table(['Step','Responsible role','Required output'],[
('1  Intake and qualify','Coordinator + drafter','Complete inputs, permitted scope, client decision maker and due date'),
('2  Resolve unknowns','Drafter + client','Written answers to scale, geometry, dimension and revision conflicts'),
('3  Estimate and agree','Coordinator','Production, review, PM and rework hours; signed scope and payment setup'),
('4  Produce','Drafter','Working DWG and a first plot using client standards'),
('5  Independent review','Reviewer','Source overlay, dimensions, layer and plot checks; resolved defect log'),
('6  Client review','Coordinator + client','One consolidated set of comments and change classification'),
('7  Release and learn','Reviewer + coordinator','Final files, transmittal, time/cost record and next-project request'),
], [119,118,267])
sub('The reviewer must check these items')
bullets([
'Units and scale match the brief. Verify against at least two independent supplied dimensions where available; log conflicting controls instead of stretching the drawing to fit.',
'Every client redline is addressed or explicitly resolved. Walls, openings and dimensions agree with the accepted source. Do not invent missing geometry.',
'Layer names, lineweights, linetypes, text, dimensions, xrefs and plot settings meet the client standard. Confirm plots are readable at the agreed paper size.',
'Reopen the delivery DWG from its delivery folder. Check for missing dependencies and inspect every PDF page before release.',
'Zero unresolved critical defects: wrong units or scale, omitted scope, unexplained geometry changes, missing references, or a misleading verification/design status.',
])
sub('Evidence and file control')
p('Keep source files read-only. Use a simple job folder with 01_Source, 02_Working, 03_Review, 04_Delivery and 05_Admin. Name releases with job, sheet, revision and date. Store a transmittal listing each released file and any unresolved client-owned assumptions.')
p('Use only client-owned or permissioned source material. Obtain specific written permission before publishing client drawings. Label internally invented sample work as demonstration work. Do not upload confidential plans to external AI services without client permission.')
p('Vector PDF import can assist production; scanned raster drawings still require tracing or other reconstruction and source verification. Autodesk distinguishes imported geometry from attached raster images. [3]','SmallA')

page('A focused sales system')
p('Start with 30 carefully qualified US firms. Treat the previously reported 100-prospect list as a research input once recovered, not as 100 sales opportunities. Verify the firm, a decision maker, a relevant recent project and a plausible recurring production need.')
table(['Priority','Customer','Reason to contact'],[
('First','Small architecture practices','Active renovation or commercial projects, recurring revisions, a principal or project manager who can review work'),
('Second','Interior-design studios','Repeated plans and client-directed layouts, established drawing standards and an identifiable technical reviewer'),
('Later','Remodelers and specialty contractors','Accept only when scope, measurement responsibility and qualified design oversight are clear'),
], [62,154,288])
sub('What to qualify in a short discovery call')
p('Ask what drawings consume their time, what arrives as source material, typical monthly volume, who makes design decisions, who accepts the work, their CAD standards, next deadline and what made previous outsourcing difficult. Ask for one representative file that can be shared securely. The objective is to scope a paid pilot.')
sub('Channel allocation')
p('Use owner relationships and manually researched direct outreach as the main channel. Reserve up to $100 total for Upwork membership and Connects after the account\'s current price and eligibility are checked. Start with 5 carefully matched proposals; expand to 10 only if fit and remaining budget support it. Avoid paid boosting in the first test.')
p('Before bidding, reopen the listing and check it is active, accepts the agency\'s location, matches the available skills, has an adequate budget and gives enough information to scope the work. Proposal counts, hires and historical client spending are signals; none proves Skarion can win the work.')
sub('Outreach cadence and tracking')
p('Research and contact about 3 to 5 qualified firms per working day once the first reviewed sample is ready. Personalize around a verified project or workflow. Follow up once after roughly 4 business days and once after 8 to 10, then pause unless they respond. Respect opt-outs and the applicable rules for the chosen outreach channel. All messages require the owner\'s authorization before sending.')
p('Track company, source URL, verified contact, fit reason, last contact, next action/date, response, pilot scope, quoted amount, outcome and reason lost. Count interested replies and scheduled discussions; do not treat email opens as qualified demand.')
sub('Platform facts that affect execution')
p('Upwork describes Agency Plus as the plan for new agency bidding and Connects purchasing. Its documentation says each agency proposal must name a member. Specialized Profiles ended May 28, 2026. Build a focused agency presence and truthful individual profiles. The current plan, Connects balance and submission readiness of Skarion\'s account still need an account check. [1, 2, 6]','SmallA')

page('The first 30 days')
p('Suggested start: November 13, 2026. The dates below are execution windows. Adjust client communications around US holiday availability. Owners are role assignments for the plan; naming a person does not dispatch work to them.')
table(['Window','Work to complete','Exit condition'],[
('Days 1 to 7\nNov 13 to 19','Owner confirms cash ceiling and roles. Drafter completes 3 sample exercises. Reviewer checks them. Coordinator prepares the offer, scope form and first 10 prospects.','3 clean sample packages, measured hours, approved scope wording and a named reviewer.'),
('Days 8 to 14\nNov 20 to 26','Review another 10 firms; begin authorized outreach and first 5 Upwork proposals. Hold discovery calls. Quote the first qualified pilot.','At least 1 qualified pilot proposal with source review and a written cost estimate.'),
('Days 15 to 21\nNov 27 to Dec 3','Complete the 30-firm list. Follow up selectively. Deliver a funded pilot and capture client feedback. Re-estimate the next job using actual time.','One accepted paid pilot or a documented diagnosis of why no pilot has sold.'),
('Days 22 to 30\nDec 4 to 12','Deliver second pilot where sold. Offer the 20 hour block to the best-fit client. Review economics, defects, sales feedback and workload.','Two paid pilots and one repeat order are the goals; record actual results and choose continue, change or pause.'),
], [102,258,144])
sub('A short weekly management review')
p('Review qualified contacts, replies, discovery calls, proposals, paid pilots, accepted deliveries and repeat orders. For each live job, review quoted versus actual hours, correction time, collection status and next due date. Spend 20 minutes on this once a week; do not build a large management system before there is volume.')
sub('Who does what')
bullets([
'Owner: positioning, price exceptions, budget and key client conversations.',
'Coordinator: qualification, estimates, schedule, client communication and records. Zihad is a possible coordinator based on the earlier discussion; confirm availability before assigning.',
'Experienced drafter: production, assumptions and recorded time.',
'Independent reviewer: benchmark review, delivery checks and defect closure. Use a qualified part-time reviewer if no suitable second person is available internally.',
])

page('Cash budget and economic discipline')
p('The incremental first-month cash ceiling is <b>$950</b>, excluding salaries already paid. Track existing staff time at a real hourly cost anyway. Having payroll already in place does not make the new service economically free.')
table(['Allocation','Maximum','Release condition'],[
('Independent review','$250','Up to $100 for samples and $150 for paid pilots; obtain the actual rate first.'),
('Commercial software reserve','$250','Only if a compliant seat or essential tool is missing. This is a reserve, not a vendor-price estimate.'),
('Domain and business email','$60','Reuse existing resources if suitable; confirm the working name before purchase.'),
('Upwork plan and Connects','$100','Check live eligibility and checkout price; combine both costs within this cap.'),
('Portfolio and basic presentation','$60','Use reviewed samples and existing tools. No paid advertising budget.'),
('Contingency','$230','Hold until actual delivery costs or a necessary launch requirement are known.'),
('Total maximum','$950','No amount is an authorization to purchase.'),
], [171,72,261])
sub('How to quote a fixed job')
p('Add drafting labor, review labor, coordination, rework allowance and job-specific expenses. Divide that cost by the fraction of the fee remaining after transaction fees and the target contribution margin. Use the actual fee for each channel.')
p('<b>Worked pilot:</b> 4 drafting hours at $10, 1 review hour at $20, 0.5 coordination hour at $20 and 1 rework hour at $10 cost $80. At a $175 selling price and an illustrative 10% transaction fee, contribution is $77.50, or 44.3%, before fixed overhead, acquisition cost and tax. These labor costs are placeholders to replace with Skarion\'s figures.')
sub('Cash and margin are different')
p('A direct 50% deposit on the $175 pilot is $87.50; it is not earned profit. Track deposits, accepted work, invoices and collections separately. The $950 budget is a cash cap, while the margin model includes the economic cost of existing labor. Do not add the entire launch budget as recurring monthly overhead or count existing salaries twice.')
p('If necessary licensing, review or other required setup exceeds the reserves, re-scope the launch or reallocate the $950 before accepting work. Do not rely on an unlicensed software seat or omit review to preserve a price.')

page('A model for recurring production')
p('The illustration below allocates 80 paid drafter hours per month at $10/hour. Sold hours are client production hours; they exclude internal review and nonbillable error correction. Assume 10% extra drafting time for rework, review equal to 15% of sold hours at $20/hour, 4 coordination hours at $20/hour, $100 recurring overhead and a 10% transaction fee. These are planning inputs, not measured Skarion costs.')
table(['Monthly measure','40 sold hours','60 sold hours','70 sold hours'],[
('Revenue at $32/hour','$1,280','$1,920','$2,240'),
('Transaction fees','$128','$192','$224'),
('Allocated drafter payroll','$800','$800','$800'),
('Independent review','$120','$180','$210'),
('Coordination plus overhead','$180','$180','$180'),
('Modeled operating surplus','$52','$568','$826'),
('Production plus rework hours','44 of 80','66 of 80','77 of 80'),
], [186,106,106,106])
p('The surplus is before owner sales time, tax, financing, one-time setup, bad debt and costs not included above. It is not a net-profit forecast. Platform fees are deducted from revenue; Upwork currently publishes a 0% to 15% contract-specific range, so replace the 10% assumption with the actual offer fee. [4]','SmallA')
sub('What the model tells us')
bullets([
'At these assumptions, break-even is about 38 sold production hours per month. The 80 paid hours support at most about 73 sold hours after allowing for 10% rework.',
'At 60 sold hours, $32/hour yields about a 29.6% modeled operating margin. About $32.22/hour is needed for a 30% margin with these exact inputs.',
'Low utilization can erase the benefit of a low hourly wage. Track allocated paid capacity separately from billable client production.',
'Review hours must have real reviewer availability. A mathematical margin does not establish the team can meet a deadline.',
])
sub('Capacity rule')
p('Reserve existing work commitments before offering blocks. Initially sell at most two 20 hour blocks unless the owner confirms more capacity. Keep about 20% of the drafter\'s allocated hours free for variation and response time. At 80 paid hours and 10% rework, that policy supports about 58 sold production hours, below the technical maximum.')
sub('When to raise prices')
p('Reprice if correction time repeatedly exceeds 10% of production, coordination exceeds the allowance, inputs remain incomplete, or the client requires heavier technical review. Include all actual hours when comparing realized margin against the pilot estimate. Do not solve a recurring pricing problem by routinely giving unpaid overtime.')

page('Ready to adapt sales material')
sub('Positioning')
p('<b>Skarion Drafting - CAD Production Support</b><br/>Layered CAD drawings and drawing revisions prepared from your supplied plans, measurements and markups. Start with a scoped paid pilot and continue with scheduled production support.')
sub('First direct message')
p('Subject: CAD production support for [firm name]')
p('Hi [name],<br/>I saw [specific verified project or relevant work]. Skarion Drafting supports drawing production from client-supplied plans and markups, including PDF-to-DWG conversion and redline updates.<br/><br/>For a suitable small package, we can scope a paid pilot at $175 to $350, with a layered DWG, plotted PDF and an assumptions log. [Insert only a completed, permissioned sample link.]<br/><br/>Do you have a drawing package coming up that would be useful to review for scope and turnaround?<br/>[Sender name and business signature]')
sub('Upwork proposal structure')
p('Your project calls for [specific deliverable]. The main issue I would clarify before drafting is [source-quality or scope question]. Our relevant example is [truthful sample description]. We would confirm the units and drawing standard, produce the DWG, check it against the source and provide a plotted PDF with an issue log. Based on [stated assumptions], the proposed [milestone / rate] is [amount] and the first draft date is [date after complete inputs]. Please confirm [one decision-critical question].')
sub('After a successful pilot')
p('The pilot took [actual production hours] plus [review/correction hours], and we delivered [accepted outputs]. For the next month, we can reserve 20 production hours for $640, scheduled across four weeks. We would keep the same drawing standards and review process. What drawing package and delivery dates should we plan first?')
sub('Minimum landing page content')
bullets([
'A clear service description and a request-a-quote action.',
'Two or three reviewed before/after samples with honest labels and publication permission.',
'Inputs required, deliverables, review process and scope boundaries.',
'A short quote form: contact, project location, drawing type, sheets, source format, units, deadline and client reviewer. Offer secure file transfer after initial contact.',
])
p('The accompanying text templates include an intake form, pilot scope, QC record, time record and lead record. Replace all bracketed fields and verify claims before use. No testimonials, project history, qualifications or guaranteed turnaround should be invented.')

page('Evidence and the next 60 days')
sub('What the evidence supports')
p('AIA reports September 2026 billings at 44.7 and average firm backlogs of 6.2 months. This supports testing flexible capacity for firms with work in progress, while acknowledging a difficult sales environment. It does not establish outsourcing demand at any particular firm. [5]')
p('The earlier discussion reports 100 Upwork postings, 100 named prospects and an emailed research package. Their underlying files and current opportunity status still need verification. Recheck any selected posting before spending Connects. Treat the proposed prices, conversion targets and budget in this playbook as experiments.')
sub('Continue or change based on paid evidence')
table(['Checkpoint','Continue when','Change course when'],[
('Day 30','Pilots are accepted, contribution meets the target and a client has bought again or committed funds.','No qualified interest after the targeted test: revise segment/message. Sales but poor margins: reprice or narrow scope. Critical defects: improve review before more volume.'),
('Days 31 to 60','Convert the best client to a block, document their standards, obtain permission for a case study and ask for one introduction.','Work is irregular: retain flexible capacity and keep acquisition focused. Do not infer demand from positive comments alone.'),
('Days 61 to 90','Consider added capacity after paid demand occupies about 70% of safe capacity for 4 weeks, collections are current and reviewer capacity is confirmed.','Avoid hiring to serve an unweighted pipeline. Require repeatable delivery economics and a credible forward workload.'),
], [77,213,214])
sub('Sources checked November 12 2026')
source('[1] Upwork - Agency Plus overview and new-project bidding', 'https://www.upwork.com/resources/agency-plus')
source('[2] Upwork - Agency Plus plan and assigned agency members', 'https://support.upwork.com/hc/en-us/articles/211062958-About-the-Agency-Plus-plan-on-Upwork')
source('[3] Autodesk - About importing PDF files', 'https://help.autodesk.com/cloudhelp/2021/ENU/AutoCAD-MAC-Core/files/GUID-76FD0B6E-CE15-4EAC-B8EA-D83E4E1233EF.htm')
source('[4] Upwork - Freelancer service fee', 'https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee')
source('[5] AIA - September 2026 Architecture Billings Index', 'https://www.aia.org/index.php/resource-center/abi-september-2026-architecture-firm-billings-slump-deepens')
source('[6] Upwork - Specialized Profiles retirement', 'https://support.upwork.com/hc/en-us/articles/115013750068-Update-to-Specialized-Profiles-What-to-know')
source('[7] California Architects Board - Building Official Information Guide', 'https://www.cab.ca.gov/docs/publications/building_official_information_guide.pdf')
p('Service titles and permitted activities vary by jurisdiction. California\'s board, for example, restricts advertising that implies unlicensed architectural practice. Confirm the project state\'s requirements and the client professional\'s responsibilities before marketing or accepting regulated scope. A drafting disclaimer by itself does not establish an exemption. [7]','SmallA')

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica',8)
    canvas.setFillColor(colors.HexColor('#64748B'))
    canvas.drawString(54,29,'Skarion Drafting  |  Launch playbook  |  November 12, 2026')
    canvas.drawRightString(558,29,str(doc.page))
    canvas.restoreState()

doc=SimpleDocTemplate(str(PDF), pagesize=letter, rightMargin=54,leftMargin=54,topMargin=48,bottomMargin=48,
                      title='Skarion Drafting Launch Playbook',author='Skarion Engineering')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(PDF)
print(f'Created {PDF} | {len(reader.pages)} pages')
for i, pg in enumerate(reader.pages,1):
    text=pg.extract_text() or ''
    print(f'Page {i}: {len(text)} characters | {text.splitlines()[0]}')
