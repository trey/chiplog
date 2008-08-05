import datetime
from django.db import models
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

    def is_today(self):
        """
        Returns ``True`` if the event takes place today, ``False``
        otherwise.
        
        Got this from http://python-pownce-api.googlecode.com/svn-history/r28/trunk/pownce.py
        """
        return self.created.date() == datetime.date.today()
