from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import date_based, list_detail, create_update
from django.conf import settings
from chiplog.models import *
from chiplog.forms import EntryForm

def entry_list(request, page=0):
    if request.POST:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/chiplog/')
        else:
            return render_to_response('entry_form.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL})
    else:
        return list_detail.object_list(
            request,
            queryset = Entry.objects.all(),
            template_object_name = 'entry',
            template_name = 'entry_list.html',
            paginate_by = 10,
            page = page,
            extra_context = {'form': EntryForm}
        )
entry_list = permission_required('entries.can_add', login_url='/admin/')(entry_list)

def entry_delete(request, object_id):
    return create_update.delete_object(
        request,
        object_id = object_id,
        model = Entry,
        template_name = 'entry_confirm_delete.html',
        post_delete_redirect = '/chiplog/',
    )
entry_delete = permission_required('entries.can_delete', login_url='/admin/')(entry_delete)

def entry_create(request):
    return create_update.create_object(
        request,
        model = Entry,
        template_name = 'entry_form.html',
        post_save_redirect = '/chiplog/',
    )
entry_create = permission_required('entries.can_add', login_url='/admin/')(entry_create)

def entry_update(request, object_id):
    return create_update.update_object(
        request,
        object_id = object_id,
        model = Entry,
        template_name = 'entry_form.html',
        post_save_redirect = '/chiplog/',
    )
entry_update = permission_required('entries.can_update', login_url='/admin/')(entry_update)
