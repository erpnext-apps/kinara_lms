app_name = "kinara_lms"
app_title = "Kinara LMS"
app_publisher = "Visage Holdings and Finance Private Limited)"
app_description = "LMS for Kinara Capital"
app_email = "help@kinaracapital.com"
app_license = "MIT"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kinara_lms/css/kinara_lms.css"
# app_include_js = "/assets/kinara_lms/js/kinara_lms.js"

# include js, css files in header of web template
# web_include_css = "/assets/kinara_lms/css/kinara_lms.css"
# web_include_js = "/assets/kinara_lms/js/kinara_lms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "kinara_lms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Loan Partner": "public/js/lending/loan_partner.js",
	"Loan": "public/js/lending/loan.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "kinara_lms.utils.jinja_methods",
#	"filters": "kinara_lms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "kinara_lms.install.before_install"
after_install = "kinara_lms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "kinara_lms.uninstall.before_uninstall"
# after_uninstall = "kinara_lms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "kinara_lms.utils.before_app_install"
# after_app_install = "kinara_lms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "kinara_lms.utils.before_app_uninstall"
# after_app_uninstall = "kinara_lms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kinara_lms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Customer": "kinara_lms.overrides.customer_master.CustomerMaster",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Loan Product": {
		"validate": "kinara_lms.overrides.loan_product.validate_loan_product_code",
	},
	"Address": {
		"validate": "kinara_lms.overrides.address.kinara_address_validate",
	},
	"Contact": {
		"validate": "kinara_lms.overrides.contact.validate_contact",
	},
	"Loan": {
		"after_insert": "kinara_lms.overrides.loan.created_loan_related_docs",
		"autoname": "kinara_lms.overrides.loan.override_name",
		"validate": "kinara_lms.overrides.loan.validate_customer_type",
	},
	"Loan Partner": {
		"validate": "kinara_lms.overrides.loan_partner.validate_loan_partner",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"kinara_lms.tasks.all"
#	],
#	"daily": [
#		"kinara_lms.tasks.daily"
#	],
#	"hourly": [
#		"kinara_lms.tasks.hourly"
#	],
#	"weekly": [
#		"kinara_lms.tasks.weekly"
#	],
#	"monthly": [
#		"kinara_lms.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "kinara_lms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "kinara_lms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "kinara_lms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["kinara_lms.utils.before_request"]
# after_request = ["kinara_lms.utils.after_request"]

# Job Events
# ----------
# before_job = ["kinara_lms.utils.before_job"]
# after_job = ["kinara_lms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"kinara_lms.auth.validate"
# ]
# fixtures = [
#     {"dt": "Custom Field", "filters": [
#         [
#             "name", "in", [
#                 "Loan-custom_individual_applicant",
#                 "Loan-custom_guarantors",
#                 "Loan-custom_co_applicants",
#             ]
#         ]
#     ]}
# ]

fixtures = [
    {"dt": "Property Setter", "filters": [
        [
            "name", "in", [
                "Customer-customer_type-options",
            ]
        ]
    ]}
]