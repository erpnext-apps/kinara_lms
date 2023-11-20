# Copyright (c) 2023, Visage Holdings and Finance Private Limited) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LoanPDC(Document):
	def validate(self):
		if self.type == "PDC":
			if self.emi is None:
				frappe.throw("EMI is Mandatory")
			if self.loan_repayment_schedule is None:
				frappe.throw("Loan Repayment Schedule is Mandatory")
			if self.amount is None:
				frappe.throw("Amount is Mandatory")
			if self.cheque_date is None:
				frappe.throw("Cheque Date is Mandatory")
