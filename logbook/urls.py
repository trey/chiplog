from django.conf.urls.defaults import *
from django.views.generic import list_detail
from views import *
from models import Entry

logbook_list = {
    'queryset': Entry.objects.all(),
    'template_name': 'log_list.html',
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, logbook_list),
    (r'^new/$', add_entry),
)
