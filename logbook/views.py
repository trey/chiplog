from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from logbook.forms import LogForm

def add_entry(request):
    if request.POST == 'POST':
        entry = Entry()
        form = LogForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = LogForm(instance=entry)
        return render_to_response('log_home.html', {'form': form})
