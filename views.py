from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import date_based, list_detail, create_update
from django.template import RequestContext
from django.core.urlresolvers import reverse
from chiplog.models import *
from chiplog.forms import EntryForm

def entry_list(request, page=0):
    if request.POST:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('chiplog_index'))
        else:
            return render_to_response('entry_form.html', {'form': form}, context_instance=RequestContext(request))
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

def entry_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id = object_id,
        queryset = Entry.objects.all(),
        template_name = 'entry_detail.html'
    )
entry_detail = permission_required('entries.can_add', login_url='/admin/')(entry_detail)

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

def search(request):
    if request.GET:
        search_term = '%s' % request.GET['s']
        if len(search_term) != 0:
            entry_list = Entry.objects.filter(body__icontains=search_term)
            context = {'entry_list': entry_list, 'search_term':search_term}
            return render_to_response('entry_search.html', context, context_instance=RequestContext(request))
        else:
            message = 'Search term was too vague. Please try again.'
            context = {'message':message}
            return render_to_response('entry_search.html', context, context_instance=RequestContext(request))
    else:
        return render_to_response('entry_search.html', {}, context_instance=RequestContext(request))
search = permission_required('entries.can_add', login_url='/admin/')(search)
