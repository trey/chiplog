from django.db import models
from tagging.fields import TagField
import tagging

class Entry(models.Model):
    """
    A Logbook Entry
    """
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags    = TagField()

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.body
