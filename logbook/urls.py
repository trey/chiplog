from django.conf.urls.defaults import *
from django.views.generic import list_detail
from views import *
from models import Entry

logbook_list = {
    'queryset': Entry.objects.all(),
}

urlpatterns = patterns('',
    (r'^new/$', add_entry),
    (r'^$', list_detail.object_list, logbook_list),
)
