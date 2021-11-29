from . import __version__ as app_version

app_name = "delabeling"
app_title = "Delabeling"
app_publisher = "gross innovate and contributors"
app_description = "tailor fit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "spryngmanaged@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/delabeling/css/delabeling_app.css"
app_include_js = "/assets/delabeling/js/delabeling.js"

# include js, css files in header of web template
web_include_css = "/assets/delabeling/css/delabeling_web.css"
# web_include_js = "/assets/delabeling/js/delabeling.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "delabeling/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

after_migrate = ['delabeling.events.api.whitelabel_patch']

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "delabeling.install.before_install"
# after_install = "delabeling.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "delabeling.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"delabeling.tasks.all"
# 	],
# 	"daily": [
# 		"delabeling.tasks.daily"
# 	],
# 	"hourly": [
# 		"delabeling.tasks.hourly"
# 	],
# 	"weekly": [
# 		"delabeling.tasks.weekly"
# 	]
# 	"monthly": [
# 		"delabeling.tasks.monthly"
# 	]
# }

# Testing
# -------  
boot_session = "delabeling.events.api.boot_session"

# before_tests = "delabeling.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "delabeling.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "delabeling.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"delabeling.auth.validate"
# ]
override_whitelisted_methods = {
	"frappe.utils.change_log.show_update_popup": "delabeling.events.api.ignore_update_popup"
}

