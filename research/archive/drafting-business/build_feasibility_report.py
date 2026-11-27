from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'stress_test_results.json').read_text(encoding='utf-8'))
USER=DATA['user_calibrated']
PDF=ROOT.parent/'output'/'pdf'/'Skarion_Drafting_Feasibility_Stress_Test.pdf'
PDF.parent.mkdir(parents=True,exist_ok=True)
styles={
 'title':ParagraphStyle('title',fontName='Helvetica-Bold',fontSize=24,leading=28,spaceAfter=13),
 'h1':ParagraphStyle('h1',fontName='Helvetica-Bold',fontSize=19,leading=23,spaceAfter=12),
 'h2':ParagraphStyle('h2',fontName='Helvetica-Bold',fontSize=11.5,leading=15,spaceBefore=10,spaceAfter=5,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=10.5,leading=14.2,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=8.8,leading=11.7,spaceAfter=6,textColor=colors.HexColor('#475569')),
 'cell':ParagraphStyle('cell',fontName='Helvetica',fontSize=9.3,leading=12.5),
 'head':ParagraphStyle('head',fontName='Helvetica-Bold',fontSize=9.3,leading=12.5,textColor=colors.white)}
story=[]
def p(t,s='body'): story.append(Paragraph(t,styles[s]))
def sub(t):p(t,'h2')
def page(t):story.append(PageBreak());p(t,'h1')
def table(headers,rows,widths):
    data=[[Paragraph(escape(str(x)),styles['head']) for x in headers]]
    data += [[Paragraph(escape(str(x)).replace('\n','<br/>'),styles['cell']) for x in row] for row in rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#193549')),
      ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F2F5F7')]),
      ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#D9D9D9')),('VALIGN',(0,0),(-1,-1),'TOP'),
      ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
      ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.extend([t,Spacer(1,8)])
def money(v):return ('-' if v<0 else '')+'$'+f'{abs(v):,.0f}'
def money2(v):return ('-' if v<0 else '')+'$'+f'{abs(v):,.2f}'
def source(i,title,url):p(f'[{i}] <link href="{escape(url)}" color="#1E587D">{escape(title)}</link>','small')

p('Skarion Drafting<br/>Feasibility Stress Test','title')
p('November 12, 2026 | Revised entry strategy and exhaustive economic tests','small')
p('<b>Verdict: commercially plausible at the reported BDT 40,000 monthly drafter cost, with a realistic case for low-price entry.</b> The main remaining tests are client acquisition, repeat purchases, review cost and delivery quality. Free entry can be a controlled acquisition expense.')
p(f'The reported cost converts to about <b>${USER["monthly_usd"]:.0f}/month</b> at Bangladesh Bank\'s November 12 reference of BDT 124.75/USD. Assuming 160 paid hours, that is about <b>${USER["hourly_usd"]:.2f}/hour</b>. Available hours and any costs beyond the reported BDT 40,000 still need confirmation. Retail conversion and transfer fees may differ. [7]')
p(f'The model evaluated <b>{DATA["total_grid_cases"]:,} discrete scenarios</b>, including a separate run using the reported monthly cost. These are economic and sales sensitivity tests, not completed customer experiments, CAD delivery benchmarks or an estimated probability of business success.','small')
sub('What changes from the first launch plan')
p('Replace the $175 minimum entry offer and the requirement for every pilot to earn 40% contribution with a controlled acquisition test. Try a $0, $25 or $49 small, defined task. Track the subsidy and subsequent paid work. Keep the $175-$350 package available for larger scopes; its size should not be given away by default.')
sub('Market evidence checked for this assessment')
table(['Observed source','Published terms or activity','Implication'],[
('Praxis Drawings [1]','$49 first sheet; from $95 for conversion; 20 hours for $400.','A discounted introduction and recurring blocks already exist. Asking prices do not prove the provider\'s sales or margins.'),
('Upwork PDF to CAD [2]','$5-$15/hour; 50+ proposals; 3 hires shown.','There is purchasing activity and substantial price competition. The actual contract rates were not disclosed.'),
('Upwork architecture firm [3]','$12-$30/hour; 6+ months; 20-50 proposals; 4 interviews.','Recurring demand is advertised; hiring and Skarion fit are not established.'),
('Upwork residential interiors [4]','$6-$8/hour; 1 hire shown; ongoing redline work.','Some real demand is too cheap for a managed agency unless costs and workflow support it.'),
], [127,166,211])
p('These are selected examples, not a representative market sample. Upwork observations came from public search results; direct page opens can be blocked and activity may be stale. Reopen a listing in the account before bidding. No completed-sale average or winning-proposal claim is inferred.','small')

page('What low entry prices actually cost')
p('The important variable is the amount of work included. A small sample can be an economical demonstration; a full drawing package can consume the marketing budget before the client has shown any intention to purchase.')
table(['Entry price','Small sample contribution','Larger pilot contribution'],[
 (money(r['price']),money2(r['sample_contribution']),money2(r['full_pilot_contribution']))
 for r in USER['entry_contributions']
], [112,196,196])
p('Contribution above is after delivery labor and an illustrative 3% payment fee, before acquisition effort and fixed overhead. All cost inputs are assumptions.','small')
sub('Small sample costing')
p(f'Allow 1.5 production hours at the implied ${USER["hourly_usd"]:.2f}/hour, 25% additional drafting time for correction, 0.5 review hour at $20/hour and 0.25 coordination hour at $20/hour. Total allocated delivery cost is <b>${USER["sample_delivery_cost"]:.2f}</b>. This is a clean drawing excerpt or a contained redline task, not any entire floor plan. Review and coordination costs remain assumptions.')
sub('Larger pilot costing')
p(f'Allow 4 production hours, 1 drafting correction hour, 1 review hour at $20/hour and 0.5 coordination hour at $20/hour. Total allocated cost is <b>${USER["full_pilot_delivery_cost"]:.2f}</b>. At $49, contribution is about $7.51 before acquisition and overhead. This makes a low-price introduction more credible than under the earlier $10/hour labor assumption.')
p('These per-job figures allocate only the hours used. If the drafter is idle for the remainder of the month, the salary must still be paid. The next page charges the business for the full reported monthly cost.','small')
sub('A free sample needs an explicit boundary')
p('Offer one sample per qualified firm, agree the deliverable in writing, and stop when the production allowance is exhausted. Resolve unknown dimensions with the client; do not silently invent them. State the price policy for subsequent work before the sample begins. Do not condition free work on a favorable review or pretend a demonstration is a paid client project.')
sub('Use the right channel')
p('Use the free sample experiment with independently sourced direct prospects. For Upwork, use an existing portfolio and a funded paid test: Upwork prohibits clients asking for free work, and its minimum-price and payment rules still apply. Do not move an Upwork lead off-platform to run the free experiment. [5]')

page('The recurring business must cover all costs')
p('Both columns below charge the full BDT 40,000 drafter cost, about $321/month. They also include 10% rework, review equal to 20% of sold hours at $20/hour, coordination equal to 10% at $20/hour, $150 sales labor, $100 overhead and a 10% payment/platform fee. The reviewer and coordination assumptions are deliberately costed separately; their actual costs are unknown.')
rows=[]
for rate in [10,15,20,25]:
    vals=[next(v['profit'] for v in USER['monthly_scenarios'] if v['rate']==rate and v['sold_hours']==h and v['reviewer_cost']==20 and v['uplift']==0) for h in [56,112]]
    rows.append([f'${rate}/hour']+[money(v) for v in vals])
table(['Selling rate','56 sold hours per month','112 sold hours per month'],rows,[140,182,182])
p('Values are monthly modeled operating surplus or loss, before tax and one-time launch costs. They are not cash balances or measured Skarion profits. The fee input is a stress assumption; Upwork publishes a 0%-15% contract-specific range. [6]','small')
sub('Practical conclusions')
p('<b>$15-$20/hour is plausible with sufficient volume.</b> At 112 sold hours, this conservative review-cost scenario leaves about $269-$773/month. At 56 sold hours, $15/hour loses about $151 and $20/hour leaves about $101. Low salary helps; unused capacity still matters.')
p('<b>The result survives a moderate cost cushion at higher utilization.</b> Adding 25% to the reported drafter cost reduces monthly surplus by about $80. At 112 sold hours, the $20/hour case still leaves about $693. Lower-cost qualified review improves the result further; it has not been assumed as a fact.')
p('<b>Capacity is a separate constraint.</b> The 112 sold hours require 123.2 drafter hours with rework, plus 22.4 reviewer hours and 11.2 coordination hours. This fits a 160-hour drafter month with a 20% reserve, but actual availability alongside existing commitments is unknown. Do not sell that capacity until it is confirmed.')
sub('Failures the tests expose')
p('A larger scope hidden behind a low sheet price, extensive correction cycles, unused paid capacity, and manual prospecting all erode margin. Free entry does not repair a negative recurring contribution. Raising volume when repeat work loses money increases the loss.')
sub('How the model should change with real information')
p('Confirm whether BDT 40,000 includes all employment costs, record the actual available hours, and measure reviewer, coordination and sales effort. Staff already paid for other work can reduce incremental cash needs; count only genuinely spare capacity and avoid allocating the same hours to two businesses.')

page('When free work pays back')
p('At the reported drafter cost, consider <b>10 completed small samples</b> at about $18.76 delivery cost each, $15 acquisition cost per completed sample and $100 allocated overhead. This assumes relatively efficient acquisition, not a cold-outreach benchmark. The free cohort costs about <b>$437.58</b> economically.')
p('A subsequent 20-hour block billed at $20/hour produces $400 revenue. Deduct 3% fees, 22 drafting hours at the implied $2.00/hour, 4 reviewer hours at $20, 2 coordination hours at $20, and $25 overhead. The block contributes about <b>$198.91</b>. Reserved idle payroll is not included here; the monthly model tests it separately.')
table(['Entry offer','Cohort deficit before repeat work','20 hour paid blocks to recover'],[
('$0', '$437.58','3 blocks'),('$25','$195.08','1 block'),('$49','Already $37.72 positive','0; repeat demand is still unproven'),
('$99','Already $522.72 positive','0; repeat demand is still unproven'),
], [97,196,211])
sub('Retention matters more than sample popularity')
p('Three clients buying one block each, or one client buying three blocks, cover the modeled free cohort. At an assumed 20% independent trial-to-paid conversion rate, payback probability is about 32% in the one-block case and 89% in the three-block case. Those are conditional calculations, not measured success odds.')
p('At $15/hour for repeat work, the block contributes about $101.91 and the free cohort needs five blocks to recover. At $10/hour, contribution falls to about $4.91 and recovery takes 90 blocks. Free entry works much better when the next order has a healthy contribution.')
sub('Cold prospecting can overturn the attractive example')
p('Assume 200 qualified contacts, 10 minutes of research/contact effort each at $15/hour, 10% replying, half of replies accepting a trial and 20% of trials becoming repeat customers. Add 15 minutes of discovery per response. That produces 10 expected trials, 2 expected repeat clients and <b>$575 in sales effort</b>, not $150.')
p('With free samples and three repeat blocks at $20/hour per converted client, the expected result is about <b>+$331</b> after the modeled delivery and overhead costs. If clients buy only one block, the result falls to about <b>-$465</b>. Lower labor cost makes the experiment plausible; retention and acquisition efficiency still determine whether it works.')
p('The models use no discounted cash-flow assumption and do not value referrals or testimonials as revenue. Later orders must be completed and paid to count toward realized payback.','small')

page('The real experiment to run next')
p('The desk tests support a bounded market experiment. They cannot establish whether this drafter meets client standards, whether buyers will reply, or whether a free trial converts to a paid relationship.')
table(['Step','Execution','Evidence to collect'],[
('1  Delivery benchmark','Complete 3 permissioned sample exercises and independent review. Time every activity.','Production, review, correction, missing-input time and critical defects.'),
('2  Comparable offers','Assign 60 qualified direct firms across $0, $25 and $49 offers, 20 per arm. Balance firm types.','Same small scope, follow-up cadence, turnaround and follow-on pricing policy in every arm.'),
('3  Bound the test','Complete at most 10 trial packages initially; no more than 4 from one arm. Stop at the cost or hour limit below.','Count all offers, responses, acceptances, refusals and capacity deferrals.'),
('4  Ask for paid work','After delivery, quote the next actual task using measured costs. Follow up once about the next package.','Paid follow-on orders at the intended regular price, not verbal interest.'),
('5  Observe retention','Review at 30 and 60 days. Extend only if results justify the remaining budget.','A second paid order, actual contribution and cumulative acquisition payback.'),
], [85,222,197])
sub('Budget limits')
p('Keep additional cash spending within the existing $950 first-month ceiling. Separately cap the acquisition experiment at <b>$650 of economic cost</b>, including allocated staff and sales time, or <b>30 team delivery hours</b>, whichever comes first. These limits overlap: the $650 is not extra authorization on top of $950. Stop earlier if actual reviewer or software costs require it.')
sub('What counts as progress')
p('Continue when samples meet the client\'s standards, at least two trial clients buy follow-on work at prices with positive measured contribution, and at least one buys again. These are management checkpoints, not a statistically validated pass/fail test. Investigate source quality, target segment, trust, turnaround and sales execution before assuming price is the only issue.')
p('A 60-contact test is directional. At a hypothetical 1% contact-to-repeat conversion rate, 60 contacts have only about a 45% chance of producing even one repeat customer. Thirty contacts have about a 26% chance. No orders in a small outreach batch do not prove the business cannot work.')
sub('Recommendation')
p('Proceed with a small free or discounted trial experiment. Keep recurring work costed honestly, quote larger scopes separately, and prioritize customers with a credible next drawing package. Set regular prices from measured delivery economics; willingness to work for free should fund learning, not conceal an indefinitely unprofitable service.')

page('Method and reproducibility')
table(['Module','Exhaustive combinations','Inputs varied'],[
('Fixed-price jobs',f'{DATA["fixed_jobs"]["count"]:,}','Price $0-$350; production 0.5-12 h; labor $2-$20/h; rework 0%-100%; review 10%-50%; reviewer $10-$30/h; PM 0.25-1 h; fees 0%-15%; acquisition $0-$50.'),
('Monthly capacity',f'{DATA["monthly"]["count"]:,}','Rate $5-$40; paid hours 80/160; sold hours 10-160; labor $2-$20; rework 0%-50%; review 10%-30%; reviewer $15/$25; fees 3%/10%/15%; overhead $100/$300/$600.'),
('Trial payback',f'{DATA["trial_cohorts"]["count"]:,}','Entry $0-$175; labor $2-$20; trial 0.5-6 h; acquisition $0-$150/trial; repeat conversion 5%-75%; repeat rate $10-$30; 1/2/3/6 repeat blocks.'),
('Acquisition funnel',f'{DATA["funnel"]["count"]:,}','30-500 contacts; reply 1%-20%; trial acceptance 10%-75%; repeat conversion 5%-50%; research 5-20 min; entry $0/$25/$49/$99; repeat rate $20/$25/$30; 1/3 blocks.'),
('BDT cost calibration',f'{USER["count"]:,}','Full BDT 40,000/month; FX 115/124.75/135; cost uplift 0%/25%/50%; capacity 40/80/160 h; rates $5-$32; reviewer $3-$20; rework 10%-50%; fees and overhead varied.'),
], [105,106,293])
p('The exact discrete values, formulas and aggregate counts are stored in stress_test_results.json. stress_tests.py reproduces the run using the Python standard library. Reference calculations, impossible-capacity cases, negative repeat margins, zero conversion and monotonic price behavior were checked. Counts show coverage of selected assumptions; aggregate pass fractions must not be described as the probability of business success.','small')
p('The modules answer different questions and their profits must not be added together. Monthly results charge reserved payroll. Trial/funnel results charge used delivery hours and specified overhead allocations. Probability calculations assume independent, identical client outcomes and fixed retention; correlated demand and varying customer quality can make them optimistic. Free work may change both acceptance and retention, and no price-elasticity curve was invented.','small')
sub('Sources checked November 12 2026')
source(1,'Praxis Drawings pricing and introductory offer','https://drawings.3dpraxisstudio.com/pricing/')
source(2,'Upwork Converting PDF drawings to CAD','https://www.upwork.com/freelance-jobs/apply/Converting-pdf-drawings-CAD_~022109913728450104628/')
source(3,'Upwork AutoCAD Draftsman for Architecture Projects','https://www.upwork.com/freelance-jobs/apply/AutoCAD-Draftsman-for-Architecture-Projects_~022119898056382648104/')
source(4,'Upwork AutoCAD Drafter for Residential Projects','https://www.upwork.com/freelance-jobs/apply/AutoCAD-Drafter-for-Residential-Projects_~022109699792052227380/')
source(5,'Upwork prohibited jobs including requests for free work','https://support.upwork.com/hc/en-us/articles/1500007578942-What-kind-of-jobs-aren-t-allowed-on-Upwork')
source(6,'Upwork contract-specific service fees','https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee')
source(7,'Bangladesh Bank November 12 exchange-rate reference','https://www.bb.org.bd/en/index.php/econdata/exchangerate')

def footer(c,d):
    c.saveState();c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#64748B'))
    c.drawString(54,29,'Skarion Drafting  |  Feasibility stress test  |  November 12, 2026')
    c.drawRightString(558,29,str(d.page));c.restoreState()
SimpleDocTemplate(str(PDF),pagesize=letter,leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=48,
                  title='Skarion Drafting Feasibility Stress Test',author='Skarion Engineering').build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(PDF)
print(f'{PDF} | {len(reader.pages)} pages')
for i,pg in enumerate(reader.pages,1):print(i,len(pg.extract_text() or ''))
