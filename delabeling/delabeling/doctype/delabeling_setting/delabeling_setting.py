# Copyright (c) 2021, gross innovate and contributors and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe.model.document import Document 
from frappe.utils import cint 
from delabeling.events.api import get_frappe_version

class DelabelingSetting(Document):
	''' pass '''
	def validate(self):
		#deplaylabel_app_name
		print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n got here for main sales \n\n\n\n\n\n\n\n')
		if cint(get_frappe_version()) >= 13:
			if self.deplaylabel_app_name:
				#frappe.db.set_value("System Settings", "System Settings", "app_name", self.deplaylabel_app_name )
				frappe.db.set_value("System Settings", "System Settings", "app_name", "Onegross" )
				print(f'\n\n\n\n\n {self.deplaylabel_app_name}\n\n\n\n')
			else:
				if "erpnext" in frappe.get_installed_apps():
					frappe.db.set_value("System Settings", "System Settings", "app_name", "ERPNext" )
				else:
					frappe.db.set_value("System Settings", "System Settings", "app_name", "Frappe" )

