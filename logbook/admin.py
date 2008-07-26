from django.contrib import admin
from logbook.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'updated',)
    list_filter   = ('created', 'updated',)
    search_fields = ('body',)

admin.site.register(Entry, EntryAdmin)
