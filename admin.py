from django.contrib import admin
from chiplog.admin import EntryAdmin
from chiplog.model import Entry

class AdminSite(admin.AdminSite):
    pass

site = AdminSite()
