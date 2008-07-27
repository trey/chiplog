from django.contrib import admin
from logbook.admin import EntryAdmin
from logbook.model import Entry

class AdminSite(admin.AdminSite):
    pass

site = AdminSite()
