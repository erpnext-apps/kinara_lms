from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.desk.page.setup_wizard.setup_wizard import make_records


KINARA_CUSTOM_FIELDS = {
	"Customer": [
		{
			"fieldname": "customer_urn",
			"label": "Customer URN",
			"fieldtype": "Data",
			"insert_after": "customer_name",
			"unique": 1,
			"reqd": 1,
		},
	],
}


def after_install():
	create_custom_fields(KINARA_CUSTOM_FIELDS, ignore_validate=True)
	make_fixtures()


def make_fixtures():
	records = [
		# Bank Account Types
		{"doctype": "Bank Account Type", "account_type": "Disbursement"},
		{"doctype": "Bank Account Type", "account_type": "Collections"},
		{"doctype": "Bank Account Type", "account_type": "Disbursement & Collections"},
	]

	make_records(records)
