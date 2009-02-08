from django.contrib import admin
from models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'tags',)
    list_filter   = ('created', 'updated', 'tags',)
    search_fields = ('body',)
    date_hierarchy = 'created'

admin.site.register(Entry, EntryAdmin)
