from django.conf.urls.defaults import *
from django.views.generic import create_update
from models import Entry

chiplog_delete = {
    'model': Entry,
    'template_name': 'delete.html',
    'post_delete_redirect': '/chiplog/',
}
chiplog_save = {
    'model': Entry,
    'template_name': 'create_read_update.html',
    'extra_context': { 'entry_list': Entry.objects.all },
    'post_save_redirect': '/chiplog/',
}

urlpatterns = patterns('',
    (r'^$', create_update.create_object, chiplog_save),
    (r'^edit/(?P<object_id>\d+)/$', create_update.update_object, chiplog_save),
    (r'^delete/(?P<object_id>\d+)/$', create_update.delete_object, chiplog_delete)
)
