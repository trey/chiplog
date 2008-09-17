import datetime
from django.db import models
from django.db.models import permalink
from tagging.fields import TagField
import tagging

class Entry(models.Model):
    """
    A Chiplog Entry
    """
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags    = TagField()

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['-created']

    def __unicode__(self):
        return self.body

    def get_absolute_url(self):
        return ('chiplog_detail', [str(self.id)])
    get_absolute_url = permalink(get_absolute_url)
