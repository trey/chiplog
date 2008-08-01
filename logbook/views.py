from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from logbook.forms import LogForm

@permission_required('logbook.add_entry')
def add_entry(request):
    """
    Add new entries and view archive of entries.
    """
    if request.POST:
        form = LogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/logbook')
        # else:
            # Errors and validation message taken care of for you.  Neat.
    else:
        form = LogForm()
    return render_to_response('log_home.html', {'form': form})
