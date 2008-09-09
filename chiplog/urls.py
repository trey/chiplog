from django.conf.urls.defaults import *
from chiplog import views

urlpatterns = patterns('',
    url(r'^$',
        view=views.entry_list,
        name='chiplog_index'),

    url(r'^page/(?P<page>\w)/$',
        view=views.entry_list,
        name='chiplog_index_paginated'),

    url(r'^new/$',
        view=views.entry_create,
        name='chiplog_create'),

    url(r'^edit/(?P<object_id>\d+)/$',
        view=views.entry_update,
        name='chiplog_update'),

    url(r'^delete/(?P<object_id>\d+)/$',
        view=views.entry_delete,
        name='chiplog_delete'),
)
