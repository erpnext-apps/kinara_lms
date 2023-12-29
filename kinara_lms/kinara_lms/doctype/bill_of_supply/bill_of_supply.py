# Copyright (c) 2023, Visage Holdings and Finance Private Limited) and contributors
# For license information, please see license.txt


import frappe
import datetime
from frappe.model.document import Document

class BillofSupply(Document):
    def before_save(self):
        loan_id = self.loan_id
        loan_doc = frappe.get_doc("Loan", loan_id)
        customer_urn = loan_doc.applicant
        company_name = loan_doc.company
        self.loan_amount = loan_doc.loan_amount
        loan_installment_date = self.loan_installment_date

        principal_amount_query = frappe.db.sql("""
            SELECT ld.demand_amount, ld.paid_amount, ld.sales_invoice
            FROM `tabLoan Demand` AS ld
            WHERE ld.loan = "{}" AND ld.demand_date = "{}" AND ld.demand_type = "EMI" AND ld.demand_subtype = "Principal"
            LIMIT 1;
        """.format(loan_id, loan_installment_date))

        if principal_amount_query:
            print(principal_amount_query)
            self.principal_amount = principal_amount_query[0][0] - principal_amount_query[0][1]


        interest_amount_query = frappe.db.sql("""
            SELECT ld.demand_amount, ld.paid_amount
            FROM `tabLoan Demand` AS ld
            WHERE ld.loan = "{}" AND ld.demand_date = "{}" AND ld.demand_type = "EMI" AND ld.demand_subtype = "Interest"
            LIMIT 1;
        """.format(loan_id, loan_installment_date))

        if interest_amount_query:
            print(interest_amount_query)
            self.interest_amount = interest_amount_query[0][0] - interest_amount_query[0][1]

        if principal_amount_query and interest_amount_query:
            self.total_amount = self.principal_amount + self.interest_amount
        
        if not principal_amount_query[0][2]:
            where_clause = f"""WHERE si.loan = "{loan_id}" AND si.customer = "{customer_urn}" """
        else:
            where_clause = f"""WHERE si.name = "{principal_amount_query[0][2]}" """
        sales_invoice_query = frappe.db.sql(f"""
            SELECT si.custom_applicant_name, si.customer_name, si.name, si.company_gstin, si.customer_address, si.billing_address_gstin, si.company_address
            FROM `tabSales Invoice` AS si
            {where_clause}
            LIMIT 1;""")
        
        if sales_invoice_query:
            self.applicant = sales_invoice_query[0][0]
            self.customer = sales_invoice_query[0][1]
            self.ti_number = sales_invoice_query[0][2]
            self.company_gstin = sales_invoice_query[0][3]

        company_address_query = frappe.db.sql("""
            SELECT ad.address_line1, ad.address_line2, ad.city, ad.state, ad.country, ad.pincode, ad.gstin, ad.gst_state_number
            FROM `tabAddress` AS ad
            WHERE ad.name = "{}"
            LIMIT 1;
        """.format(sales_invoice_query[6]))
        if company_address_query:     
            self.company_state_code = company_address_query[0][7] or ""
            self.place_of_supply = company_address_query[0][2] or "" + ", " + company_address_query[0][3] or ""
            self.posting_date = datetime.datetime.now().date()
        
        customer_address_query = frappe.db.sql("""
            SELECT ad.address_line1, ad.address_line2, ad.city, ad.state, ad.country, ad.pincode, ad.gstin, ad.gst_state_number
            FROM `tabAddress` AS ad
            WHERE ad.name = "{}"
            LIMIT 1;
        """.format(sales_invoice_query[4]))
        if customer_address_query:
            self.customer_gstin = sales_invoice_query[5] or ""
            self.customer_address = customer_address_query[0][0] or "" + ", " + customer_address_query[0][1] or "" + ", " + customer_address_query[0][2] or "" + ", " + customer_address_query[0][3] or "" + ", " + customer_address_query[0][4] or "" + ", " + customer_address_query[0][5] or ""
        







        






        










