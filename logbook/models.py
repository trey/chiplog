from django.db import models
from tagging.fields import TagField
import tagging

class Entry(models.Model):
    """
    A Logbook entry
    """
    body    = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags    = TagField()

    class Admin:
        list_display = ('body', 'created', 'updated')
        list_filter   = ('created', 'updated')
        search_fields = ('body')

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.body
