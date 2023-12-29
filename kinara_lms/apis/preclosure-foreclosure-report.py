import frappe
import json


@frappe.whitelist()
def get_preclosure_foreclosure_pdf(**kwargs):
    body = json.loads(frappe.request.data)
    doc = frappe.new_doc('Preclosure-Foreclosure Report')
    doc.loan_account_number = body["loan"]
    proposed_closure_date = body["as_on_date"].split("-")
    doc.proposed_closure_date = proposed_closure_date[2]+"-"+proposed_closure_date[1]+"-"+proposed_closure_date[0]
    doc.payment_type = body["payment_type"]
    doc.save()
    frappe.db.commit()
    base_url = frappe.utils.get_url()
    pdf_url = f"{base_url}/api/method/frappe.utils.print_format.download_pdf?doctype=Preclosure-Foreclosure%20Report&name={doc.name}&format=Loan%20Preclosure%20Foreclosure&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en"
    return{"pdf": pdf_url}