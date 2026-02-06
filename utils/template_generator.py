"""
Template Generator for SME-Friendly Contract Templates
Generates standardized contracts based on best practices for Indian SMEs
"""

import json
import streamlit as st
from datetime import datetime
from typing import Dict, List, Optional
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
import os

class TemplateGenerator:
    def __init__(self):
        self.templates = {
            "employment": self._generate_employment_agreement,
            "vendor": self._generate_vendor_contract,
            "lease": self._generate_lease_agreement,
            "partnership": self._generate_partnership_deed,
            "service": self._generate_service_contract,
            "nda": self._generate_nda_agreement,
            "consultancy": self._generate_consultancy_agreement
        }
        
        # Template parameters with default values
        self.default_params = {
            "company_name": "ABC Enterprises",
            "employee_name": "John Doe",
            "vendor_name": "XYZ Suppliers",
            "property_address": "123 Business Street, Mumbai",
            "partner_names": ["Partner A", "Partner B"],
            "service_description": "Digital Marketing Services",
            "start_date": datetime.now().strftime("%d %B, %Y"),
            "duration": "12 months",
            "compensation": "₹50,000 per month",
            "jurisdiction": "Mumbai, Maharashtra",
            "confidentiality_period": "3 years"
        }
    
    def generate_template(self, template_type: str, custom_params: Dict = None) -> str:
        """Generate contract template based on type and custom parameters"""
        if template_type not in self.templates:
            raise ValueError(f"Template type '{template_type}' not supported")
        
        # Merge default params with custom params
        params = self.default_params.copy()
        if custom_params:
            params.update(custom_params)
        
        # Generate template
        template_content = self.templates[template_type](params)
        
        return template_content
    
    def _generate_employment_agreement(self, params: Dict) -> str:
        """Generate Employment Agreement Template"""
        template = f"""
EMPLOYMENT AGREEMENT

This Employment Agreement ("Agreement") is made on {params['start_date']}

BETWEEN

{params['company_name']}, a company incorporated under the laws of India, 
having its registered office at [Company Address] (hereinafter referred to as the "Employer")

AND

{params['employee_name']}, residing at [Employee Address] (hereinafter referred to as the "Employee")

WHEREAS the Employer desires to employ the Employee, and the Employee desires to accept such employment;

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:

1. APPOINTMENT AND TERM
   1.1 The Employer hereby appoints the Employee as [Designation], and the Employee accepts such appointment.
   1.2 The term of employment shall commence on {params['start_date']} and continue for a period of {params['duration']}, unless terminated earlier as per this Agreement.
   1.3 After the initial term, this Agreement may be extended by mutual written consent.

2. DUTIES AND RESPONSIBILITIES
   2.1 The Employee shall perform the duties of [Designation] and such other duties as may be reasonably assigned by the Employer.
   2.2 The Employee shall devote full business time and attention to the performance of duties.
   2.3 The Employee shall comply with all policies and procedures of the Employer.

3. COMPENSATION
   3.1 The Employee shall be paid a gross salary of {params['compensation']}, payable on the [Day] of each month.
   3.2 The salary includes basic salary, house rent allowance, and other applicable components as per company policy.
   3.3 The Employee shall be entitled to statutory benefits including Provident Fund, ESIC (if applicable), and gratuity as per law.

4. CONFIDENTIALITY
   4.1 The Employee shall not disclose any confidential information of the Employer during or after employment.
   4.2 Confidential information includes business plans, customer lists, financial information, and trade secrets.
   4.3 This obligation shall continue for {params['confidentiality_period']} after termination of employment.

5. INTELLECTUAL PROPERTY
   5.1 All work product created by the Employee during employment shall be the sole property of the Employer.
   5.2 The Employee assigns all rights, title, and interest in such work product to the Employer.
   5.3 The Employee shall assist the Employer in securing intellectual property rights.

6. TERMINATION
   6.1 Either party may terminate this Agreement by giving [30 days] written notice.
   6.2 The Employer may terminate immediately for cause, including misconduct, negligence, or breach of agreement.
   6.3 Upon termination, the Employee shall return all company property and confidential information.

7. NON-COMPETE AND NON-SOLICITATION
   7.1 During employment and for [6 months] after termination, the Employee shall not engage in competing business.
   7.2 The Employee shall not solicit clients, employees, or contractors of the Employer for [1 year] after termination.

8. GOVERNING LAW AND DISPUTE RESOLUTION
   8.1 This Agreement shall be governed by the laws of India.
   8.2 Any disputes shall be subject to the exclusive jurisdiction of courts in {params['jurisdiction']}.
   8.3 Parties agree to attempt mediation before pursuing litigation.

9. MISCELLANEOUS
   9.1 This Agreement constitutes the entire understanding between parties.
   9.2 Any amendments must be in writing and signed by both parties.
   9.3 Notices shall be sent to the addresses mentioned above.

IN WITNESS WHEREOF, the parties have executed this Agreement on the date first above written.

_________________________
For {params['company_name']}
(Name)
(Designation)

_________________________
{params['employee_name']}
Employee
        """
        return template
    
    def _generate_vendor_contract(self, params: Dict) -> str:
        """Generate Vendor/Supplier Contract Template"""
        template = f"""
VENDOR SUPPLY AGREEMENT

This Vendor Supply Agreement ("Agreement") is made on {params['start_date']}

BETWEEN

{params['company_name']}, a company incorporated under the laws of India, 
having its registered office at [Company Address] (hereinafter referred to as the "Buyer")

AND

{params['vendor_name']}, having its principal place of business at [Vendor Address] 
(hereinafter referred to as the "Vendor")

WHEREAS the Buyer desires to purchase goods/services from the Vendor, and the Vendor desires to supply such goods/services;

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:

1. SCOPE OF SUPPLY
   1.1 The Vendor shall supply [Description of Goods/Services] as per specifications in Annexure A.
   1.2 All goods shall conform to the quality standards specified and applicable Indian standards.
   1.3 Services shall be performed with due care, skill, and diligence.

2. TERM AND DELIVERY
   2.1 This Agreement shall commence on {params['start_date']} and continue for {params['duration']}.
   2.2 Delivery shall be made as per the schedule in Annexure B.
   2.3 Time is of the essence for all delivery obligations.

3. PRICE AND PAYMENT
   3.1 The total contract value shall be [Total Amount] inclusive of all taxes.
   3.2 Payment terms: [e.g., 30% advance, 60% on delivery, 10% after acceptance].
   3.3 All payments shall be made within [30 days] of invoice submission.
   3.4 Taxes: GST and other applicable taxes shall be charged separately.

4. QUALITY AND INSPECTION
   4.1 Goods shall be subject to inspection upon delivery.
   4.2 The Buyer may reject non-conforming goods within [7 days] of delivery.
   4.3 The Vendor shall replace rejected goods at no additional cost.

5. WARRANTIES
   5.1 The Vendor warrants that goods are free from defects for [Warranty Period].
   5.2 Services shall be free from errors and conform to specifications.
   5.3 All warranties are in addition to statutory warranties under Indian law.

6. INDEMNIFICATION
   6.1 The Vendor shall indemnify the Buyer against all losses arising from:
       a) Defective goods/services
       b) Intellectual property infringement
       c) Violation of laws
   6.2 Liability shall be limited to the contract value, except for willful misconduct.

7. TERMINATION
   7.1 Either party may terminate for material breach with [30 days] notice to cure.
   7.2 The Buyer may terminate for convenience with [30 days] written notice.
   7.3 Upon termination, the Vendor shall deliver all completed work and materials.

8. FORCE MAJEURE
   8.1 Neither party shall be liable for delays due to force majeure events.
   8.2 Force majeure includes natural disasters, government actions, and epidemics.
   8.3 Affected party must notify within [48 hours] of occurrence.

9. CONFIDENTIALITY
   9.1 Parties shall maintain confidentiality of business information.
   9.2 This obligation shall survive termination for {params['confidentiality_period']}.

10. GOVERNING LAW AND DISPUTE RESOLUTION
    10.1 This Agreement shall be governed by Indian law.
    10.2 Disputes shall be resolved through arbitration in {params['jurisdiction']}.
    10.3 The arbitral award shall be final and binding.

IN WITNESS WHEREOF, the parties have executed this Agreement on the date first above written.

_________________________
For {params['company_name']}
(Name)
(Designation)

_________________________
For {params['vendor_name']}
(Name)
(Designation)

ANNEXURE A: Specifications
ANNEXURE B: Delivery Schedule
ANNEXURE C: Commercial Terms
        """
        return template
    
    def _generate_lease_agreement(self, params: Dict) -> str:
        """Generate Commercial Lease Agreement Template"""
        template = f"""
COMMERCIAL LEASE AGREEMENT

This Lease Agreement ("Agreement") is made on {params['start_date']}

BETWEEN

[Lessor Name], residing at [Lessor Address] (hereinafter referred to as the "Lessor")

AND

{params['company_name']}, a company incorporated under the laws of India, 
having its registered office at [Company Address] (hereinafter referred to as the "Lessee")

WHEREAS the Lessor is the absolute owner of the premises at {params['property_address']};
WHEREAS the Lessee desires to take the premises on lease for commercial purposes;

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:

1. DEMISED PREMISES
   1.1 The Lessor lets and the Lessee takes on lease the premises at {params['property_address']}.
   1.2 The premises shall be used only for [Business Purpose - e.g., Office, Retail Shop, Warehouse].
   1.3 The total built-up area is approximately [Area] square feet.

2. TERM
   2.1 The lease term shall be {params['duration']} commencing from {params['start_date']}.
   2.2 The Lessee shall have an option to renew for further terms, subject to mutual agreement.

3. RENT AND DEPOSIT
   3.1 Monthly rent: {params['compensation']}, payable in advance by the [Day] of each month.
   3.2 Security deposit: [Amount - typically 3-6 months rent], refundable without interest at lease end.
   3.3 Rent escalation: [e.g., 10% increase every 3 years] as per mutual agreement.
   3.4 All payments shall be made via bank transfer to the Lessor's account.

4. MAINTENANCE AND REPAIRS
   4.1 The Lessor shall be responsible for structural repairs and major maintenance.
   4.2 The Lessee shall be responsible for routine maintenance, repairs due to misuse, and interior upkeep.
   4.3 The Lessee shall maintain the premises in good condition.

5. UTILITIES AND TAXES
   5.1 The Lessee shall pay all utilities: electricity, water, gas, internet, etc.
   5.2 Property tax shall be paid by the Lessor.
   5.3 The Lessee shall obtain necessary trade licenses and permits.

6. ALTERATIONS
   6.1 The Lessee may make non-structural alterations with prior written consent of Lessor.
   6.2 All fixtures installed by Lessee shall become property of Lessor upon termination.
   6.3 The Lessee shall not make changes that affect structural integrity.

7. INSURANCE
   7.1 The Lessor shall maintain fire insurance for the building structure.
   7.2 The Lessee shall maintain insurance for contents, business interruption, and public liability.
   7.3 Both parties shall provide insurance certificates upon request.

8. TERMINATION
   8.1 Either party may terminate with [3 months] written notice.
   8.2 The Lessor may terminate immediately for:
       a) Non-payment of rent for [2] consecutive months
       b) Illegal activities on premises
       c) Material breach of terms
   8.3 Upon termination, Lessee shall hand over premises in original condition.

9. GOVERNING LAW
   9.1 This Agreement shall be governed by the Transfer of Property Act and Indian law.
   9.2 Jurisdiction for disputes: Courts in {params['jurisdiction']}.

10. REGISTRATION
    10.1 This Agreement shall be registered as per applicable state laws if lease exceeds [11 months].
    10.2 Registration charges shall be borne [as per mutual agreement or state law].

IN WITNESS WHEREOF, the parties have executed this Agreement on the date first above written.

_________________________
[Lessor Name]
Lessor

Witness:
1. ____________________
   Name:
   Address:

_________________________
For {params['company_name']}
(Name)
(Designation)

Witness:
1. ____________________
   Name:
   Address:
        """
        return template
    
    def _generate_partnership_deed(self, params: Dict) -> str:
        """Generate Partnership Deed Template"""
        partners_list = "\n".join([f"   {i+1}. {partner}" for i, partner in enumerate(params['partner_names'])])
        
        template = f"""
PARTNERSHIP DEED

This Partnership Deed ("Deed") is made on {params['start_date']}

BETWEEN

{partners_list}

(all collectively referred to as "Partners" and individually as "Partner")

WHEREAS the Partners desire to carry on business in partnership on the terms and conditions herein;

NOW, THEREFORE, the Partners hereby agree as follows:

1. NAME AND BUSINESS
   1.1 The partnership shall carry on business under the name and style of "{params['company_name']}".
   1.2 The principal place of business shall be at [Business Address].
   1.3 The nature of business shall be: [Description of Business Activities].

2. CAPITAL CONTRIBUTION
   2.1 The initial capital of the partnership shall be ₹[Total Capital].
   2.2 Partners shall contribute in the following proportions:
       {self._generate_partner_contributions(params['partner_names'])}
   2.3 Additional capital contributions shall require unanimous consent.

3. PROFIT AND LOSS SHARING
   3.1 Profits and losses shall be shared in proportion to capital contributions.
   3.2 Drawings by Partners shall not exceed [Percentage]% of expected annual profits.
   3.3 Financial year: 1st April to 31st March.

4. MANAGEMENT AND AUTHORITY
   4.1 All Partners shall participate in management.
   4.2 Major decisions require consent of Partners representing [75]% of capital.
   4.3 Banking operations shall require joint signatures of [Number] Partners.

5. DUTIES AND RESPONSIBILITIES
   5.1 Each Partner shall devote [Time Commitment] to partnership business.
   5.2 Partners shall not engage in competing business without consent.
   5.3 Partners shall maintain accurate books of accounts.

6. ADMISSION OF NEW PARTNERS
   6.1 Admission of new Partners requires unanimous consent of existing Partners.
   6.2 New Partners shall execute this Deed with amendments as necessary.
   6.3 Terms of admission shall be fair and reasonable.

7. RETIREMENT AND EXPULSION
   7.1 A Partner may retire with [6 months] written notice.
   7.2 A Partner may be expelled for misconduct or breach by majority consent.
   7.3 Settlement amount shall be paid as per valuation by Chartered Accountant.

8. DISSOLUTION
   8.1 The partnership may be dissolved by unanimous consent or as per law.
   8.2 Upon dissolution, assets shall be sold and proceeds distributed after settling liabilities.
   8.3 Final accounts shall be prepared by a Chartered Accountant.

9. DISPUTE RESOLUTION
   9.1 Partners shall attempt amicable settlement of disputes.
   9.2 Failing settlement, disputes shall be referred to arbitration in {params['jurisdiction']}.
   9.3 The arbitration shall be governed by the Arbitration and Conciliation Act, 1996.

10. MISCELLANEOUS
    10.1 This Deed shall be registered with Registrar of Firms as per Partnership Act.
    10.2 Any amendment requires written consent of all Partners.
    10.3 Partners shall maintain confidentiality of partnership affairs.

IN WITNESS WHEREOF, the Partners have executed this Deed on the date first above written.

SIGNATURES OF PARTNERS:

{self._generate_partner_signatures(params['partner_names'])}

WITNESSES:

1. _________________________
   Name:
   Address:

2. _________________________
   Name:
   Address:
        """
        return template
    
    def _generate_service_contract(self, params: Dict) -> str:
        """Generate Service Contract Template"""
        template = f"""
SERVICE AGREEMENT

This Service Agreement ("Agreement") is made on {params['start_date']}

BETWEEN

{params['company_name']}, a company incorporated under the laws of India, 
having its registered office at [Company Address] (hereinafter referred to as the "Client")

AND

[Service Provider Name], having its principal place of business at [Service Provider Address]
(hereinafter referred to as the "Service Provider")

WHEREAS the Client desires to engage the Service Provider for {params['service_description']};

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:

1. SERVICES
   1.1 The Service Provider shall provide the following services:
       {params['service_description']}
   1.2 Detailed scope of work is attached as Annexure A.
   1.3 Services shall be performed with professional standards and due diligence.

2. TERM
   2.1 This Agreement shall commence on {params['start_date']} and continue for {params['duration']}.
   2.2 Either party may renew for additional terms by mutual written agreement.

3. COMPENSATION
   3.1 The total contract value shall be {params['compensation']}.
   3.2 Payment schedule: [e.g., Monthly invoices, Milestone-based payments]
   3.3 All amounts are exclusive of GST which shall be charged separately.
   3.4 Late payments shall attract interest at [1.5]% per month.

4. DELIVERABLES AND TIMELINES
   4.1 Key deliverables are specified in Annexure B with timelines.
   4.2 The Service Provider shall provide regular progress reports [weekly/monthly].
   4.3 The Client shall provide timely feedback and necessary inputs.

5. ACCEPTANCE CRITERIA
   5.1 Deliverables shall be accepted if they meet specifications in Annexure A.
   5.2 The Client shall provide acceptance or rejection within [7 days] of delivery.
   5.3 Rejected deliverables shall be rectified within [reasonable time].

6. INTELLECTUAL PROPERTY
   6.1 Pre-existing IP of either party remains their respective property.
   6.2 IP developed during this engagement shall belong to [Client/Service Provider/Joint].
   6.3 The Service Provider grants necessary licenses for use of deliverables.

7. CONFIDENTIALITY
   7.1 Both parties shall maintain confidentiality of each other's information.
   7.2 This obligation shall survive termination for {params['confidentiality_period']}.
   7.3 Exclusions: Information publicly available or independently developed.

8. WARRANTIES AND LIABILITY
   8.1 The Service Provider warrants services will be performed professionally.
   8.2 Liability shall be limited to the contract value.
   8.3 Neither party shall be liable for indirect or consequential damages.

9. TERMINATION
   9.1 Either party may terminate with [30 days] written notice.
   9.2 Termination for cause: Material breach not cured within [15 days] notice.
   9.3 Upon termination, Service Provider shall deliver all completed work.

10. GOVERNING LAW
    10.1 This Agreement shall be governed by Indian law.
    10.2 Jurisdiction for disputes: Courts in {params['jurisdiction']}.

IN WITNESS WHEREOF, the parties have executed this Agreement on the date first above written.

_________________________
For {params['company_name']}
(Name)
(Designation)

_________________________
For [Service Provider Name]
(Name)
(Designation)

ANNEXURES:
A. Detailed Scope of Work
B. Deliverables and Timelines
C. Commercial Terms
        """
        return template
    
    def _generate_nda_agreement(self, params: Dict) -> str:
        """Generate Non-Disclosure Agreement Template"""
        template = f"""
NON-DISCLOSURE AGREEMENT

This Non-Disclosure Agreement ("Agreement") is made on {params['start_date']}

BETWEEN

{params['company_name']}, having its office at [Company Address] (hereinafter referred to as the "Disclosing Party")

AND

[Receiving Party Name], having its office at [Receiving Party Address] (hereinafter referred to as the "Receiving Party")

WHEREAS the parties desire to explore a potential business relationship;
WHEREAS such exploration may require disclosure of confidential information;

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:

1. CONFIDENTIAL INFORMATION
   1.1 "Confidential Information" means all non-public information disclosed by Disclosing Party.
   1.2 Includes business plans, financial data, customer lists, technical specifications, trade secrets.
   1.3 Excludes information that is:
       a) Publicly available
       b) Independently developed
       c) Received from third parties without restriction

2. OBLIGATIONS
   2.1 Receiving Party shall:
       a) Use Confidential Information only for evaluating potential business relationship
       b) Maintain confidentiality with at least same degree of care as its own confidential information
       c) Disclose only to employees/agents with need to know who are bound by similar obligations
   2.2 Receiving Party shall not reverse engineer, copy, or disclose to third parties.

3. TERM
   3.1 This Agreement shall remain in effect for {params['duration']}.
   3.2 Confidentiality obligations shall survive termination for {params['confidentiality_period']}.
   3.3 Either party may terminate with [30 days] written notice.

4. RETURN OF INFORMATION
   4.1 Upon request or termination, Receiving Party shall return or destroy all Confidential Information.
   4.2 Receiving Party may retain one archival copy for compliance purposes.
   4.3 Legal counsel may retain copies as required by law.

5. NO LICENSE
   5.1 This Agreement does not grant any license or rights to Confidential Information.
   5.2 All IP rights remain with Disclosing Party.
   5.3 No obligation to proceed with business relationship.

6. GOVERNING LAW
   6.1 This Agreement shall be governed by Indian law.
   6.2 Disputes shall be subject to exclusive jurisdiction of courts in {params['jurisdiction']}.

7. MISCELLANEOUS
   7.1 This Agreement constitutes the entire understanding.
   7.2 Notices shall be in writing and sent to addresses above.
   7.3 If any provision is invalid, remaining provisions shall remain in effect.

IN WITNESS WHEREOF, the parties have executed this Agreement on the date first above written.

_________________________
For {params['company_name']}
(Name)
(Designation)

_________________________
For [Receiving Party Name]
(Name)
(Designation)
        """
        return template
    
    def _generate_consultancy_agreement(self, params: Dict) -> str:
        """Generate Consultancy Agreement Template"""
        template = f"""
CONSULTANCY AGREEMENT

This Consultancy Agreement ("Agreement") is made on {params['start_date']}

BETWEEN

{params['company_name']}, having its office at [Company Address] (hereinafter referred to as the "Client")

AND

[Consultant Name], residing at [Consultant Address] (hereinafter referred to as the "Consultant")

WHEREAS the Client desires to engage the Consultant for professional services;

NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:

1. SERVICES
   1.1 The Consultant shall provide consultancy services as described in Annexure A.
   1.2 Services shall be performed with professional skill and diligence.
   1.3 The Consultant is an independent contractor, not an employee.

2. TERM AND TERMINATION
   2.1 This Agreement shall commence on {params['start_date']} and continue for {params['duration']}.
   2.2 Either party may terminate with [30 days] written notice.
   2.3 The Client may terminate immediately for breach or unsatisfactory performance.

3. COMPENSATION
   3.1 The Consultant shall be paid {params['compensation']} for services rendered.
   3.2 Invoices shall be submitted [monthly/upon completion] and paid within [15 days].
   3.3 The Consultant is responsible for all taxes on compensation received.

4. CONFIDENTIALITY
   4.1 The Consultant shall maintain confidentiality of Client information.
   4.2 This obligation shall continue for {params['confidentiality_period']} after termination.
   4.3 The Consultant shall not use confidential information for personal benefit.

5. INTELLECTUAL PROPERTY
   5.1 All work product created under this Agreement shall belong to the Client.
   5.2 The Consultant assigns all rights to the Client.
   5.3 The Consultant shall assist in securing IP rights as needed.

6. REPRESENTATIONS AND WARRANTIES
   6.1 Consultant has necessary skills and authority to perform services.
   6.2 Services will not infringe third-party rights.
   6.3 Consultant will comply with all applicable laws.

7. LIMITATION OF LIABILITY
   7.1 Consultant's liability limited to fees received under this Agreement.
   7.2 Neither party liable for indirect, special, or consequential damages.
   7.3 Consultant not liable for business decisions made based on advice.

8. INDEPENDENT CONTRACTOR
   8.1 Consultant is responsible for own taxes, insurance, and benefits.
   8.2 Consultant may engage assistants at own expense.
   8.3 Client shall not control manner or method of work.

9. GOVERNING LAW
   9.1 This Agreement shall be governed by Indian law.
   9.2 Jurisdiction: Courts in {params['jurisdiction']}.

IN WITNESS WHEREOF, the parties have executed this Agreement on the date first above written.

_________________________
For {params['company_name']}
(Name)
(Designation)

_________________________
[Consultant Name]
Consultant
        """
        return template
    
    def _generate_partner_contributions(self, partner_names: List[str]) -> str:
        """Generate partner contribution section"""
        contributions = ""
        for i, partner in enumerate(partner_names):
            contributions += f"       {partner}: ₹[Amount] ([Percentage]%)\n"
        return contributions
    
    def _generate_partner_signatures(self, partner_names: List[str]) -> str:
        """Generate partner signature section"""
        signatures = ""
        for partner in partner_names:
            signatures += f"{partner}: _________________________\n\n"
        return signatures
    
    def export_to_pdf(self, template_content: str, filename: str = "contract_template.pdf"):
        """Export template to PDF format"""
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Custom styles
        styles.add(ParagraphStyle(
            name='ContractStyle',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            alignment=TA_JUSTIFY
        ))
        
        styles.add(ParagraphStyle(
            name='TitleStyle',
            parent=styles['Heading1'],
            fontSize=16,
            alignment=TA_CENTER,
            spaceAfter=20
        ))
        
        # Build PDF content
        content = []
        lines = template_content.strip().split('\n')
        
        for line in lines:
            if line.strip() == "":
                content.append(Spacer(1, 12))
            elif line.isupper() and len(line.strip()) > 20:
                # This is likely a title/section header
                content.append(Paragraph(line.strip(), styles['TitleStyle']))
            else:
                content.append(Paragraph(line.strip(), styles['ContractStyle']))
        
        doc.build(content)
        return filename
    
    def get_template_parameters_form(self):
        """Generate Streamlit form for template customization"""
        
        st.subheader("Customize Your Contract Template")
        
        col1, col2 = st.columns(2)
        
        with col1:
            template_type = st.selectbox(
                "Select Contract Type",
                list(self.templates.keys()),
                format_func=lambda x: x.replace('_', ' ').title()
            )
            
            company_name = st.text_input("Company Name", "ABC Enterprises")
            start_date = st.date_input("Start Date", datetime.now())
            duration = st.selectbox("Duration", ["3 months", "6 months", "12 months", "24 months", "36 months"])
            
        with col2:
            if template_type == "employment":
                employee_name = st.text_input("Employee Name", "John Doe")
                compensation = st.text_input("Monthly Salary", "₹50,000")
            elif template_type == "vendor":
                vendor_name = st.text_input("Vendor Name", "XYZ Suppliers")
                compensation = st.text_input("Contract Value", "₹5,00,000")
            elif template_type == "lease":
                property_address = st.text_input("Property Address", "123 Business Street, Mumbai")
                compensation = st.text_input("Monthly Rent", "₹75,000")
            elif template_type == "partnership":
                partner_count = st.number_input("Number of Partners", min_value=2, max_value=10, value=2)
                partner_names = []
                for i in range(partner_count):
                    partner_names.append(st.text_input(f"Partner {i+1} Name", f"Partner {chr(65+i)}"))
                compensation = st.text_input("Total Capital", "₹10,00,000")
            elif template_type == "service":
                service_description = st.text_area("Service Description", "Digital Marketing Services")
                compensation = st.text_input("Service Fee", "₹1,00,000 per month")
            else:
                compensation = st.text_input("Compensation/Value", "To be negotiated")
            
            jurisdiction = st.selectbox("Jurisdiction", 
                ["Mumbai, Maharashtra", "Delhi, NCR", "Bangalore, Karnataka", 
                 "Chennai, Tamil Nadu", "Hyderabad, Telangana", "Kolkata, West Bengal"])
        
        confidentiality = st.selectbox("Confidentiality Period", ["1 year", "2 years", "3 years", "5 years", "Perpetual"])
        
        # Build parameters dictionary
        params = {
            "company_name": company_name,
            "start_date": start_date.strftime("%d %B, %Y"),
            "duration": duration,
            "compensation": compensation,
            "jurisdiction": jurisdiction.split(',')[0],  # Just the city
            "confidentiality_period": confidentiality
        }
        
        # Add template-specific parameters
        if template_type == "employment":
            params["employee_name"] = employee_name
        elif template_type == "vendor":
            params["vendor_name"] = vendor_name
        elif template_type == "lease":
            params["property_address"] = property_address
        elif template_type == "partnership":
            params["partner_names"] = partner_names
        elif template_type == "service":
            params["service_description"] = service_description
        
        return template_type, params


# Streamlit UI integration for template generator
def render_template_generator_ui():
    """Render the template generator UI in Streamlit"""
    
    st.title("📝 Contract Template Generator")
    st.markdown("Generate SME-friendly contract templates customized for your business")
    
    generator = TemplateGenerator()
    
    # Step 1: Template Selection and Customization
    template_type, params = generator.get_template_parameters_form()
    
    if st.button("Generate Template", type="primary"):
        with st.spinner(f"Generating {template_type.replace('_', ' ').title()}..."):
            # Generate template
            template_content = generator.generate_template(template_type, params)
            
            # Display template
            st.subheader("Generated Contract Template")
            with st.expander("View Full Template", expanded=True):
                st.code(template_content, language=None)
            
            # Export options
            st.subheader("📥 Export Options")
            col1, col2 = st.columns(2)
            
            with col1:
                # Download as Text
                st.download_button(
                    label="📄 Download as Text",
                    data=template_content,
                    file_name=f"{template_type}_contract.txt",
                    mime="text/plain"
                )
            
            with col2:
                # Generate PDF
                pdf_path = f"{template_type}_template.pdf"
                try:
                    generator.export_to_pdf(template_content, pdf_path)
                    with open(pdf_path, "rb") as pdf_file:
                        st.download_button(
                            label="📑 Download as PDF",
                            data=pdf_file,
                            file_name=pdf_path,
                            mime="application/pdf"
                        )
                    # Clean up
                    os.remove(pdf_path)
                except Exception as e:
                    st.error(f"PDF generation failed: {e}")
            
            # Template Tips
            st.info("💡 **Template Usage Tips:**\n"
                   "1. Fill in all [bracketed] information\n"
                   "2. Review jurisdiction-specific requirements\n"
                   "3. Consult with legal advisor before signing\n"
                   "4. Keep signed copies with all parties")


# Standalone testing
if __name__ == "__main__":
    # Example usage
    generator = TemplateGenerator()
    
    # Generate an employment agreement
    params = {
        "company_name": "Tech Solutions Pvt Ltd",
        "employee_name": "Rahul Sharma",
        "start_date": "15 January, 2024",
        "duration": "24 months",
        "compensation": "₹85,000 per month",
        "jurisdiction": "Bangalore"
    }
    
    template = generator.generate_template("employment", params)
    print("Generated Employment Agreement:")
    print(template)
    
    # Export to PDF
    generator.export_to_pdf(template, "employment_agreement.pdf")
    print("\nPDF generated: employment_agreement.pdf")