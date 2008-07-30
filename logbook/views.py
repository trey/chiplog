from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from logbook.forms import LogForm

def add_entry(request):
    """
    Add new entries and view archive of entries.
    """
    if request.POST:
        form = LogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        form = LogForm()
    return render_to_response('log_home.html', {'form': form})
