from models import Entry
from django import newforms as forms

LogForm = form_for_model(Entry)

def add_entry(request):
    """
    Add a Logbook Entry.
    """
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = LogForm()
        return render_to_response('log_home.html', ('form': form))
