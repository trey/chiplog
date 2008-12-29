import datetime
from django.db import models
from django.db.models import permalink
from tagging.fields import TagField
import tagging
from django.utils.translation import ugettext_lazy as _

class Entry(models.Model):
    """
    A Chiplog Entry
    """
    body    = models.TextField(_('body'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField( _('updated'), auto_now=True)
    tags    = TagField()
    
    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        ordering = ['-created']
    
    def __unicode__(self):
        return self.body
    
    @models.permalink
    def get_absolute_url(self):
        return ('chiplog_detail', [str(self.id)])
