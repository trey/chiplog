from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import date_based, list_detail, create_update
from chiplog.models import *

def entry_list(request, page=0):
    return list_detail.object_list(
        request,
        queryset = Entry.objects.all(),
        template_object_name = 'entry',
        template_name = 'read.html',
        paginate_by = 10,
    )

def entry_delete(request):
    return create_update.delete_object(
        request,
        model = Entry,
        template_name = 'delete.html',
        post_delete_redirect = '/chiplog/',
    )

def entry_create(request):
    return create_update.create_object(
        request,
        model = Entry,
        template_name = 'create_update.html',
        post_save_redirect = '/chiplog/',
    )

def entry_update(request):
    return create_update.update_object(
        request,
        model = Entry,
        template_name = 'create_update.html',
        post_save_redirect = '/chiplog/',
    )

