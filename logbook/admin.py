from django.contrib import admin
from logbook.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'tags')
    list_filter   = ('created', 'updated', 'tags')
    search_fields = ('body',)

admin.site.register(Entry, EntryAdmin)
