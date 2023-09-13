"""
Using ChatGPT I created lists of keywords for all possible industries (collected manually) listed below
programmatically via https://github.com/acheong08/ChatGPT 

industry = 'retail'
STANDARD_PROMPT = "Please list 30 common XXX document types".replace("XXX", f"{industry}")
## SPECIAL queries
'''
Can you provide synonyms to each listed type?
Can you make each line formatted like "Insurance policy": {"coverage", "protection", "plan"} ?
"Please list 30 common retail document types with their synonyms like Credit memos - {"credit notes", "credit slips", "refund slips"}
Please list 30 common retail document types with their synonyms like Credit memos - credit notes, credit slips, refund slips
'''
# DEV: check for duplicates across industries
"""

INDUSTRIES = [
    "business",
    "business services",
        #"marketing",
        #"sales",
        #"recruitment",
        #"HR",
    "legal",
        #"court",
        #"notary",
        #"mortgage",
    "retail",
        #"wholesale",
    "finance",
    "investment",
        #"private equity",
    "banking",
        #"credit",
        #"loan",
    "accounting",
        #"expenditure",
    "insurance",
        #"claims",
        #"underwriting",
        #"medical health claims",
    "healthcare",
        #"medical",
        #"pharmaceutical",
    "manufacturing",
    "government",
        #"administrative",
    "transportation",
        #"shipping",
    "travel",
        #"tourism",
        #"hospitality",
    "real estate",
    "communications",
        #"media",
        #"publishing",
    "telecommunications",
    "agriculture",
    "education",
]

ALTERNATE = ["personal", "office", "company"]

industry_results = {
    'business': {
'''
1. Business plan: {"strategy", "blueprint", "roadmap"}
2. Marketing plan: {"promotion plan", "advertising plan", "publicity plan"}
3. Financial plan: {"budget", "forecast", "projection"}
4. Sales plan: {"revenue plan", "sales strategy", "business development plan"}
5. Operation plan: {"production plan", "logistics plan", "supply chain plan"}
6. Organizational chart: {"hierarchy", "structure", "flow chart"}
7. Employee handbook: {"employee manual", "employee guide", "employee policies"}
8. Meeting minutes: {"notes", "record", "summary"}
9. Action plan: {"implementation plan", "execution plan", "activity plan"}
10. Business proposal: {"offer", "presentation", "pitch"}
11. Business case: {"analysis", "justification", "reasoning"}
12. Business letter: {"correspondence", "letterhead", "formal letter"}
13. Business report: {"analysis", "document", "research"}
14. SWOT analysis: {"strengths", "weaknesses", "opportunities", "threats"}
15. Competitive analysis: {"market research", "industry analysis", "competitor
analysis"}
16. Business model: {"revenue model", "value proposition", "customer segments"}
17. Workflow diagram: {"process flowchart", "activity diagram", "flowchart"}
18. Business plan template: {"outline", "guide", "example"}
19. Financial statement: {"balance sheet", "income statement", "cash flow
statement"}
20. Business plan executive summary: {"overview", "summary", "highlights"}
21. Business plan appendix: {"supporting documents", "references", "additional
information"}
22. Business plan cover page: {"title page", "front page", "cover letter"}
23. Non-disclosure agreement: {"confidentiality agreement", "secrecy agreement",
"NDA"}
24. Partnership agreement: {"association agreement", "joint venture agreement",
"partnership contract"}
25. Employment agreement: {"job contract", "employment contract", "work
contract"}
26. Employee contract: {"employment contract", "job contract", "work agreement"}
27. Service contract: {"agreement", "service agreement", "service level
agreement"}
28. Consulting contract: {"agreement", "consulting agreement", "consulting
services agreement"}
29. Sales contract: {"agreement", "sales agreement", "purchase agreement"}
30. Purchase order: {"order", "purchase order form", "PO"}
'''
    },
    'business services': 
'''
Chatbot: 
1. Marketing plan: {"promotion plan", "advertising plan", "publicity plan"}
2. Sales plan: {"revenue plan", "sales strategy", "business development plan"}
3. Marketing campaign: {"advertising campaign", "promotion campaign", "marketing
strategy"}
4. Sales pitch: {"presentation", "offer", "proposal"}
5. Marketing budget: {"promotion budget", "advertising budget", "marketing
expenses"}
6. Sales forecast: {"projection", "estimate", "prediction"}
7. Marketing strategy: {"plan", "tactics", "approach"}
8. Sales quota: {"target", "goal", "objective"}
9. Marketing research: {"analysis", "survey", "study"}
10. Sales funnel: {"customer journey", "sales process", "conversion process"}
11. Marketing mix: {"product", "price", "promotion", "place"}
12. Sales script: {"dialogue", "conversation", "outline"}
13. Marketing plan template: {"outline", "guide", "example"}
14. Sales proposal template: {"outline", "guide", "example"}
15. Marketing calendar: {"planner", "schedule", "timeline"}
16. Sales contract template: {"agreement", "template", "sample"}
17. Marketing report: {"analysis", "document", "research"}
18. Sales report: {"analysis", "document", "research"}
19. Marketing ROI: {"return on investment", "performance", "effectiveness"}
20. Sales performance metrics: {"key performance indicators", "metrics", "KPIs"}
21. Marketing automation: {"technology", "tools", "software"}
22. Sales enablement: {"tools", "training", "resources"}
23. Marketing objectives: {"goals", "targets", "outcomes"}
24. Sales goals: {"objectives", "targets", "outcomes"}
25. Marketing metrics: {"key performance indicators", "metrics", "KPIs"}
26. Sales metrics: {"key performance indicators", "metrics", "KPIs"}
27. Marketing funnel: {"customer journey", "marketing process", "conversion
process"}
28. Sales process: {"steps", "methodology", "approach"}
29. Marketing campaign template: {"outline", "guide", "example"}
30. Sales training: {"education", "lessons", "program"}
''',
    'legal':{
'''
1. Contract - agreement, document, understanding, terms
2. Will - testament, last will and testament, final instructions
3. Power of attorney - authorization, authorization letter, proxy,
representation
4. Lease agreement - rental agreement, tenancy agreement
5. Non-disclosure agreement - confidentiality agreement, secret agreement
6. Employment agreement - job contract, work contract
7. Partnership agreement - association agreement, joint venture agreement
8. Trust agreement - trust instrument, declaration of trust
9. Deed - property deed, conveyance
10. Mortgage - loan, loan agreement, credit
11. Promissory note - IOU, debt instrument, note
12. Release of liability - waiver, indemnity, hold harmless
13. Settlement agreement - resolution, compromise, arrangement
14. Patent - invention, intellectual property
15. Trademark - brand, logo, trademark registration
16. Copyright registration - copyright application, intellectual property
registration
17. Intellectual property license - intellectual property agreement, license
agreement
18. Bill of sale - sales contract, purchase agreement
19. Certificate of incorporation - articles of incorporation, corporation
charter
20. Bylaws - rules, regulations, articles of association
21. Operating agreement - articles of organization, management agreement
22. Nonprofit articles of incorporation - articles of association, certificate
of incorporation
23. Financial power of attorney - financial authorization, financial proxy
24. Health care power of attorney - health care authorization, health care proxy
25. Living will - advance directive, personal directive
26. Parental consent form - permission form, parental authorization
27. Guardianship papers - guardianship documents, conservatorship documents
28. Conservatorship papers - conservatorship documents, guardianship documents
29. Authorization letter - authorization, power of attorney
30. Letter of intent - statement of intent, declaration of intent, expression of
interest
'''
},
    'insurance':{
'''
1. Insurance policy - coverage, protection, plan
2. Claim form - request for payment, application for benefits
3. Proof of insurance - insurance certificate, insurance card
4. Declaration page - policy summary, coverage summary
5. Endorsement - amendment, addendum, rider
6. Coverage summary - policy summary, declaration page
7. Rider - amendment, addendum, endorsement
8. Exclusion - limitation, restriction, exception
9. Deductible - excess, co-payment
10. Premium - cost, price, rate
11. Waiver of premium - premium exemption, premium discount
12. Cancellation notice - termination notice, nonrenewal notice
13. Renewal notice - renewal invitation, renewal reminder
14. Certificate of insurance - insurance certificate, insurance card
15. Binder - temporary coverage, provisional coverage
16. Loss run - claim history, claims record
17. Risk assessment - risk evaluation, risk analysis
18. Loss control report - risk management report, safety report
19. Actuarial report - mathematical analysis, statistical analysis
20. Underwriting guidelines - underwriting rules, underwriting standards
21. Reinsurance agreement - insurance agreement, risk transfer agreement
22. Retrospective rating plan - pay-as-you-go plan, experience-rated plan
23. Captive insurance agreement - self-insurance agreement, risk retention
agreement
24. Self-insurance certificate - self-insurance approval, self-insurance
authorization
25. Fronting agreement - insurance agreement, risk transfer agreement
26. Surplus lines certificate - excess and surplus lines approval, nonadmitted
insurance approval
27. Coverage verification - insurance verification, coverage confirmation
28. Claims history report - claim record, loss history
29. Annual statement - financial statement, insurance statement
30. Experience modification factor - experience rating factor, experience mod,
mod factor
'''
    },
    'retail': 
'''
1. Invoices - {"bills", "statements", "receipts"}
2. Quotes - {"estimates", "proposals", "tenders"}
3. Purchase orders - {"buy orders", "order forms"}
4. Sales orders - {"order confirmations", "customer orders"}
5. Credit memos - {"credit notes", "credit slips", "refund slips"}
6. Debit memos - {"debit notes", "debit slips", "billing adjustments"}
7. Packing lists - {"packing slips", "shipping lists"}
8. Shipping manifests - {"manifests", "shipping reports"}
9. Waybills - {"shipping documents", "transportation documents"}
10. Bills of lading - {"shipping contracts", "freight contracts"}
11. Receiving reports - {"goods received records", "delivery reports"}
12. Request for quotation - {"RFQ", "request for proposal", "bid request"}
13. Purchase requisition - {"PR", "material requisition", "goods requisition"}
14. Return merchandise authorization - {"RMA", "return authorization", "returns
form"}
''',
    'finance': 
'''
1. Invoices - bills, billing statements
2. Credit memos - credit notes, credit slips, refund slips
3. Receipts - proof of payment, sales receipts, cash register receipts
4. Purchase orders - purchase requisitions, material requisitions
5. Sales orders - sales contracts, customer orders
6. Quotes - estimates, proposals
7. Delivery notes - packing slips, shipping lists
8. Statements - account statements, customer statements
9. Ledgers - general ledgers, accounting ledgers
10. Journals - daybooks, general journals
11. Financial reports - income statements, balance sheets, cash flow statements
12. Budgets - budget plans, financial plans
13. Bank statements - account statements, checkbook registers
14. Payroll records - employee records, salary records
15. Tax returns - income tax returns, tax forms
16. Expense reports - travel and expense reports, expense claims
17. Timesheets - attendance records, employee time sheets
18. Payslips - pay stubs, salary slips
19. Contracts - agreements, legal contracts
20. Debentures - bonds, promissory notes
21. Receivable aging - accounts receivable aging, accounts receivable summary
22. Payable aging - accounts payable aging, accounts payable summary
23. Inventory reports - stock reports, inventory lists
24. Depreciation schedules - asset depreciation schedules, fixed asset schedules
25. Capital expenditure requests - capital expenditure budgets, capital
expenditure proposals
26. Investment portfolios - asset portfolios, investment accounts
27. Mutual fund statements - investment statements, fund statements
28. 401(k) statements - retirement account statements, pension statements
29. Annuities - retirement income contracts, pension plans
30. Life insurance policies - life policies, death benefit policies
''',
    'investment': 
'''
1. Prospectus - offering memorandum, investment prospectus
2. Investment agreement - subscription agreement, investment contract
3. Confidentiality agreement - non-disclosure agreement, secrecy agreement
4. Term sheet - letter of intent, memorandum of understanding
5. Investment memo - investment proposal, investment recommendation
6. Investment policy statement - investment guidelines, investment objectives
7. Risk assessment - risk analysis, risk management plan
8. Portfolio review - investment review, portfolio analysis
9. Investment proposal - investment plan, business plan
10. Investment summary - executive summary, project summary
11. Investment presentation - pitch deck, slide deck
12. Financial projections - budget projections, financial forecast
13. Feasibility study - market research, business case
14. Valuation report - asset valuation, company valuation
15. SWOT analysis - strengths, weaknesses, opportunities, and threats analysis
16. Industry analysis - market analysis, competitive analysis
17. Competitive landscape - market share analysis, competitive positioning
18. Market trends - industry trends, market research
19. Market research report - survey report, focus group report
20. Customer demographic analysis - target market analysis, customer profiling
21. Customer needs analysis - market needs analysis, customer segmentation
22. Marketing plan - branding plan, advertising plan
23. Sales plan - revenue plan, growth plan
24. Operational plan - business plan, action plan
25. Strategic plan - business strategy, corporate strategy
26. Business model - revenue model, growth model
27. Exit strategy - divestment strategy, liquidation plan
28. Investment thesis - investment rationale, investment hypothesis
29. Investment strategy - asset allocation, portfolio management
30. Investment portfolio - asset portfolio, investment accounts.
''',
    'banking': 
'''
1. Bank statement - statement of account
2. Check - cheque
3. Deposit slip - deposit ticket
4. Credit card statement - statement of account
5. ATM receipt - cash withdrawal slip
6. Payment voucher - payment receipt
7. Transfer receipt - wire transfer receipt
8. Cashier's check - bank draft
9. Direct deposit form - direct deposit authorization form
10. Endorsement stamp - endorsement seal
11. Letter of credit - documentary credit
12. Promissory note - IOU
13. Debit memo - debit note, debit slip
14. Credit memo - credit note, credit slip, refund slip
15. ACH authorization form - electronic funds transfer authorization form
16. Electronic funds transfer confirmation - EFT confirmation
17. Wire transfer confirmation - wire confirmation
18. Bank reference letter - letter of reference
19. Bank account verification letter - bank verification letter
20. Bank certification - bank letter of certification
21. Certified check - certified bank draft
22. Bank guarantee - letter of guarantee
23. Letter of indemnity - indemnity bond
24. Bank reference number - bank transaction number
25. Bank authorization letter - authorization to debit account
26. Bank verification of deposit - BVOd
27. Stop payment order - stop payment request
28. Collection authorization form - authorization to collect payment
29. Bank reconciliation statement - reconciliation statement
30. Bank deposit slip - deposit ticket, deposit form
''',
    'accounting': 
'''
1. Invoice - bill, statement of account
2. Credit note - credit memo, credit slip, refund slip
3. Debit note - debit memo, debit slip
4. Receipt - payment receipt, cash receipt
5. Payment voucher - cash voucher, check voucher
6. Purchase order - PO
7. Sales order - SO
8. Delivery note - packing slip, shipping note
9. Purchase invoice - supplier invoice
10. Sales invoice - customer invoice
11. Accounts payable ledger - creditors ledger
12. Accounts receivable ledger - debtors ledger
13. General ledger - ledger account
14. Trial balance - T-account
15. Income statement - profit and loss statement
16. Balance sheet - statement of financial position
17. Cash flow statement - statement of cash flows
18. Statement of changes in equity - statement of retained earnings
19. Statement of comprehensive income - statement of net income
20. Chart of accounts - nominal ledger
21. Financial statement - statement of financial performance
22. Fixed asset register - fixed asset ledger
23. Depreciation schedule - depreciation table
24. Amortization schedule - amortization table
25. Accruals journal - accrued expenses journal
26. Prepayments journal - prepaid expenses journal
27. General journal - journal entry
28. Sales journal - sales ledger
29. Purchase journal - purchase ledger
30. Petty cash book - petty cash ledger
''',
    'healthcare': 
'''
1. Medical record - health record, patient record
2. Progress note - progress report, progress chart
3. History and physical exam - H&P, medical history and physical
4. Operative report - surgery report, surgical report
5. Discharge summary - discharge report, discharge note
6. Consultation report - consultation note
7. Laboratory report - lab report, pathology report
8. Radiology report - imaging report, scan report
9. Pathology report - tissue report, biopsy report
10. EKG report - ECG report
11. Echocardiogram report - echocardiography report
12. Blood gas report - arterial blood gas report
13. Blood work report - blood test report, laboratory blood test report
14. X-ray report - radiograph report
15. MRI report - magnetic resonance imaging report
16. CT scan report - computed tomography scan report
17. Ultrasound report - sonogram report
18. Immunization record - vaccination record
19. Allergy list - allergy record
20. Medication list - medication record
21. Family medical history - medical family tree
22. Health insurance card - insurance card, ID card
23. Advance directive - living will, medical power of attorney
24. Do not resuscitate order - DNR order
25. Care plan - treatment plan
26. Referral form - referral letter
27. Admission form - admission note
28. Discharge form - discharge paperwork
29. Consent form - informed consent form
30. Health assessment form - health history form, health questionnaire
''',
    'manufacturing': 
'''
1. Bill of materials (BOM): single assembly bill, assembly document, parts list
2. Process flowchart: process map, process diagram, process flow diagram
3. Work instruction: operation instruction, standard operating procedure (SOP),
procedure manual
4. Quality control plan: inspection and testing plan, quality assurance plan
5. Failure mode and effects analysis (FMEA): fault tree analysis, reliability
analysis
6. Inspection and test plan (ITP): quality control plan, quality assurance plan
7. Engineering change order (ECO): change notice, change request, engineering
change request (ECR)
8. Process control plan: production control plan, manufacturing control plan
9. Drawing: technical drawing, engineering drawing, blueprint
10. Process capability analysis: capability study, process performance analysis
11. Calibration procedure: calibration instructions, calibration manual
12. Manufacturing process plan: production process plan, process plan
13. Gage repeatability and reproducibility (R&R) study: measurement system
analysis (MSA)
14. Control plan: inspection plan, quality control plan
15. Layout drawing: plant layout, factory layout
16. Process failure mode and effects analysis (PFMEA): process FMEA, process
hazard analysis
17. Material safety data sheet (MSDS): safety data sheet (SDS)
18. Risk assessment: hazard assessment, risk analysis
19. Standard operating procedure (SOP): work instruction, operating manual,
procedure manual
20. Work order: job order, production order, manufacturing order
21. Product specification: product spec, technical specification, specifications
22. Product design: product development, engineering design
23. Tooling design: tool design, mold design, die design
24. Tolerance analysis: dimensional analysis, geometric dimensioning and
tolerancing (GD&T)
25. Process flow diagram: process map, process flowchart
26. Quality assurance plan: quality control plan, inspection and testing plan
27. Inspection report: quality control report, inspection document
28. Training manual: employee training guide, employee training manual
29. Equipment manual: machine manual, equipment operation manual
30. Maintenance schedule: maintenance plan, preventative maintenance schedule
''',
    'government': 
'''
1. Act: law, statute, regulation
2. Administrative rule: regulation, rule, order
3. Affidavit: sworn statement, sworn declaration
4. Budget: financial plan, spending plan
5. By-law: ordinance, rule, regulation
6. Certificate: diploma, award, credential
7. Code: law, statute, regulation
8. Constitution: charter, fundamental law, fundamental principles
9. Contract: agreement, deal, arrangement
10. Convention: treaty, agreement, pact
11. Declaration: statement, proclamation, announcement
12. Deed: document, instrument, agreement
13. Executive order: presidential order, directive, mandate
14. Law: act, statute, regulation
15. License: permit, authorization, certification
16. Memorandum: note, message, communication
17. Ordinance: by-law, rule, regulation
18. Permit: license, authorization, approval
19. Policy: plan, strategy, guideline
20. Protocol: agreement, treaty, pact
21. Regulation: rule, administrative rule, by-law
22. Resolution: decision, agreement, vote
23. Rule: regulation, administrative rule, by-law
24. Statute: law, act, code
25. Treaty: convention, agreement, pact
26. Verdict: decision, judgment, ruling
27. Warrant: authorization, permission, license
28. White paper: report, document, briefing
29. Will: testament, last will and testament, testamentary document
30. Writ: legal document, court order, judicial order
''',
    'transportation': 
'''
1. Bill of lading: shipping document, cargo receipt, transport document
2. Air waybill: air consignment note, air transport document, air cargo receipt
3. Packing list: cargo list, shipping list, packing slip
4. Shipping manifest: cargo manifest, cargo list, voyage manifest
5. Loading list: cargo list, packing list, shipping list
6. Export declaration: customs declaration, export document, export clearance
document
7. Import declaration: customs declaration, import document, import clearance
document
8. Freight invoice: shipping invoice, transport invoice, cargo invoice
9. Certificate of origin: origin certificate, certificate of manufacture,
certificate of production
10. Cargo insurance policy: marine insurance policy, shipping insurance policy
11. Weight and balance report: aircraft weight and balance, cargo weight and
balance
12. Dangerous goods declaration: hazardous goods declaration, hazardous
materials declaration
13. Shipper's letter of instruction: shipping instructions, cargo instructions,
consignment instructions
14. Shipping advice: cargo advice, transport advice, shipping notification
15. Charter party: ship charter, vessel charter, cargo charter
16. Marine survey report: cargo survey report, shipping survey report, vessel
survey report
17. Mate's receipt: captain's receipt, master's receipt, cargo receipt
18. Cargo surveyor's report: marine surveyor's report, shipping surveyor's
report
19. Dispatch note: shipping note, transport note, cargo note
20. Shipment tracking report: cargo tracking report, transport tracking report,
consignment tracking report
21. Waybill: transport document, cargo receipt, consignment note
22. Vehicle registration: car registration, license plate, registration plate
23. Vehicle insurance policy: auto insurance policy, car insurance policy
24. Vehicle inspection report: car inspection report, truck inspection report,
fleet inspection report
25. Vehicle title: car title, vehicle ownership document, proof of ownership
26. Fuel receipt: gas receipt, petrol receipt, diesel receipt
27. Ferry ticket: boat ticket, water transport ticket
28. Train ticket: rail ticket, railway ticket
29. Bus ticket: coach ticket, public transport ticket
30. Airline ticket: flight ticket, plane ticket, air transport ticket
''',
    'real estate': 
'''
1. Deed of trust - trust deed, mortgage deed)
2. Mortgage note - promissory note, loan note)
3. Purchase agreement - sales contract, real estate contract)
4. Escrow agreement - escrow instructions, escrow instructions form)
5. Deed - conveyance, title deed)
6. Title insurance policy - property insurance, land title insurance)
7. Closing statement - settlement statement, HUD-1 statement)
8. Inspection report - home inspection report, property inspection
report)
9. Appraisal report - property valuation, real estate appraisal)
10. Survey report - boundary survey, land survey)
11. Environmental assessment - environmental impact report,
environmental site assessment)
12. Zoning certificate - zoning compliance certificate, land use
certificate)
13. Building permit - construction permit, development permit)
14. Certificate of occupancy - occupancy permit, use and occupancy
permit)
15. Easement agreement - right-of-way agreement, access agreement)
16. Encumbrance certificate - title certificate, property certificate)
17. Restrictive covenant - restrictive deed covenant, negative
covenant)
18. Assignment of mortgage - mortgage assignment, assignment of deed of
trust)
19. Subordination agreement - subordination of mortgage, subordination
of deed of trust)
20. Release of mortgage - mortgage discharge, release of deed of trust)
21. Quitclaim deed - quitclaim conveyance, quitclaim form)
22. Warranty deed - general warranty deed, covenant deed)
23. Special warranty deed - limited warranty deed, restricted warranty
deed)
24. Grant deed - grant conveyance, grant form)
25. Lease agreement - rental agreement, tenancy agreement)
26. Sublease agreement - sublet agreement, subtenancy agreement)
27. Rent roll - rental schedule, rent ledger)
28. Tenant estoppel certificate - tenant estoppel agreement, tenant
estoppel form)
29. Landlord estoppel certificate - landlord estoppel agreement,
landlord estoppel form)
30. Notice to vacate - eviction notice, notice to quit)
''',
#     'communications': 
# '''

# ''',
    'telecommunications': 
'''
1. Service agreement (synonyms: telecom contract, service contract)
2. Service level agreement (synonyms: SLA, performance agreement)
3. Service order (synonyms: installation order, service request)
4. Service record (synonyms: service history, work order)
5. Network diagram (synonyms: topology diagram, network map)
6. Site survey report (synonyms: network survey, site audit)
7. Bill of materials (synonyms: BOM, equipment list)
8. Cable schedule (synonyms: wiring schedule, infrastructure schedule)
9. Site plan (synonyms: floor plan, network layout)
10. Rack elevation (synonyms: rack diagram, rack layout)
11. Power plan (synonyms: power distribution, power layout)
12. Test plan (synonyms: acceptance plan, verification plan)
13. Test report (synonyms: acceptance report, verification report)
14. Change management plan (synonyms: change control plan, change procedure)
15. Incident report (synonyms: service interruption report, outage report)
16. Trouble ticket (synonyms: service request, support ticket)
17. Configuration management plan (synonyms: configuration control plan,
configuration procedure)
18. Configuration record (synonyms: configuration history, configuration log)
19. Hardware inventory (synonyms: equipment inventory, device inventory)
20. Software inventory (synonyms: application inventory, license inventory)
21. Capacity plan (synonyms: growth plan, scaling plan)
22. Disaster recovery plan (synonyms: business continuity plan, disaster
prevention plan)
23. Security plan (synonyms: cybersecurity plan, network security plan)
24. Access control plan (synonyms: user access plan, authentication plan)
25. Quality of service plan (synonyms: QoS plan, performance plan)
26. Service catalog (synonyms: service list, service menu)
27. Service level objective (synonyms: SLO, performance target)
28. Service level target (synonyms: SLT, performance goal)
29. Service level indicator (synonyms: SLI, performance metric)
30. Service level agreement violation (synonyms: SLA breach, performance breach)
''',
    'agriculture': 
'''
1. Farm plan (synonyms: agriculture plan, farming plan)
2. Crop plan (synonyms: planting plan, harvest plan)
3. Irrigation plan (synonyms: water management plan, watering plan)
4. Fertilizer plan (synonyms: nutrient plan, soil amendment plan)
5. Pesticide plan (synonyms: pest management plan, weed control plan)
6. Soil test report (synonyms: soil analysis, soil health report)
7. Weather forecast (synonyms: weather prediction, weather outlook)
8. Market report (synonyms: commodity report, price report)
9. Inspection report (synonyms: farm inspection, food safety inspection)
10. Certification report (synonyms: organic certification, food safety
certification)
11. Crop insurance policy (synonyms: farm insurance, agricultural insurance)
12. Lease agreement (synonyms: farm lease, land lease)
13. Equipment lease (synonyms: machinery lease, farm equipment lease)
14. Equipment purchase agreement (synonyms: machinery purchase agreement, farm
equipment purchase agreement)
15. Seeds purchase agreement (synonyms: seed purchase order, seed contract)
16. Fertilizer purchase agreement (synonyms: fertilizer purchase order,
fertilizer contract)
17. Pesticide purchase agreement (synonyms: pesticide purchase order, pesticide
contract)
18. Crop sales contract (synonyms: grain sales contract, produce sales contract)
19. Livestock sales contract (synonyms: animal sales contract, meat sales
contract)
20. Service contract (synonyms: farm services contract, agricultural services
contract)
21. Employment contract (synonyms: farm labor contract, agricultural labor
contract)
22. Hiring plan (synonyms: labor plan, workforce plan)
23. Training plan (synonyms: farm training plan, agricultural training plan)
24. Safety plan (synonyms: farm safety plan, agricultural safety plan)
25. Environmental plan (synonyms: conservation plan, stewardship plan)
26. Transportation plan (synonyms: logistics plan, delivery plan)
27. Storage plan (synonyms: warehousing plan, inventory plan)
28. Quality plan (synonyms: product quality plan, food quality plan)
29. Traceability plan (synonyms: food traceability plan, supply chain
traceability plan)
30. Recall plan (synonyms: food recall plan, product recall plan)
''',
    'education': 
'''
1. Lesson plan (synonyms: teaching plan, instruction plan)
2. Unit plan (synonyms: course plan, curriculum plan)
3. Student handbook (synonyms: school handbook, student guide)
4. Course syllabus (synonyms: class syllabus, lesson syllabus)
5. Student planner (synonyms: homework planner, assignment planner)
6. Parent-teacher conference schedule (synonyms: parent-teacher meeting
schedule, parent-teacher appointment schedule)
7. Student progress report (synonyms: report card, academic report)
8. Student behavior report (synonyms: discipline report, conduct report)
9. Student health record (synonyms: medical record, immunization record)
10. Student enrollment form (synonyms: enrollment application, registration
form)
11. Student withdrawal form (synonyms: withdrawal request, leave of absence
form)
12. Student transfer form (synonyms: transfer request, school change form)
13. Student consent form (synonyms: permission form, authorization form)
14. Student release form (synonyms: release of information form, confidentiality
form)
15. Student identification card (synonyms: school ID, student ID)
16. Student attendance record (synonyms: attendance log, roll call)
17. Student absence excuse (synonyms: absence note, leave note)
18. Student grade book (synonyms: grade record, grade log)
19. Student portfolio (synonyms: learning portfolio, achievement portfolio)
20. Student evaluation (synonyms: performance evaluation, progress evaluation)
21. Teacher evaluation (synonyms: performance evaluation, professional
evaluation)
22. Teacher certification (synonyms: teaching certification, education
certification)
23. Teacher licensure (synonyms: teaching license, education license)
24. Teacher contract (synonyms: employment contract, teaching agreement)
25. School budget (synonyms: education budget, district budget)
26. School calendar (synonyms: academic calendar, school schedule)
27. School policy (synonyms: education policy, district policy)
28. School procedure (synonyms: education procedure, district procedure)
29. School code of conduct (synonyms: student code of conduct, school discipline
code)
30. School accreditation (synonyms: education accreditation, district
accreditation)
''',

    'personal': 
'''
1. Birth certificate (synonyms: birth record, birth certificate copy)
2. Social Security card (synonyms: Social Security number, SSN)
3. Driver's license (synonyms: driver's permit, driving license)
4. Passport (synonyms: travel document, international passport)
5. Visa (synonyms: travel visa, entry visa)
6. Green card (synonyms: permanent resident card, permanent resident status)
7. Marriage certificate (synonyms: marriage license, marriage record)
8. Divorce decree (synonyms: divorce certificate, divorce order)
9. Will (synonyms: testament, last will and testament)
10. Living will (synonyms: medical directive, advance directive)
11. Power of attorney (synonyms: POA, durable power of attorney)
12. Healthcare proxy (synonyms: medical proxy, healthcare power of attorney)
13. Credit report (synonyms: credit history, credit score)
14. Bank statement (synonyms: financial statement, account statement)
15. Pay stub (synonyms: pay slip, wage statement)
16. Tax return (synonyms: income tax return, federal tax return)
17. Tax transcript (synonyms: tax record, tax history)
18. Insurance policy (synonyms: insurance contract, insurance coverage)
19. Pension plan (synonyms: retirement plan, 401k plan)
20. Investment portfolio (synonyms: investment statement, investment holdings)
21. Education transcript (synonyms: academic transcript, school transcript)
22. Employment record (synonyms: work history, employment history)
23. Resume (synonyms: CV, curriculum vitae)
24. Cover letter (synonyms: application letter, job application letter)
25. Reference letter (synonyms: recommendation letter, personal reference)
26. Employment contract (synonyms: job contract, employment agreement)
27. Employment offer letter (synonyms: job offer letter, job offer)
28. Termination letter (synonyms: dismissal letter, firing letter)
29. Severance agreement (synonyms: separation agreement, termination agreement)
30. Non-disclosure agreement (synonyms: confidentiality agreement, secrecy
agreement)
'''
}