**Chiplog** is a simple way to enter notes that get time/date stamped. It's a way to document what you're doing without having to deal with how to manage it. It's written in Django.

Inspired by Cliff Stoll's Log Book in [Cuckoo's Egg](http://readernaut.com/trey/notes/68/).

The name is taking things back to [where the word "Log" came from in the first place](http://en.wikipedia.org/wiki/Chip_log).

Requirements

- [Django Tagging](http://code.google.com/p/django-tagging/)
- Django Markup (django.contrib.markup)
- Django Humanize (django.contrib.humanize)
- [Python Markdown](http://err.no/pymarkdown/pymarkdown.py)

---

**Installation**

In `settings.py`, add to `INSTALLED_APPS`:

	'chiplog',
	'tagging',
	'django.contrib.markup',
	'django.contrib.humanize',

In `urls.py`:

	urlpatterns = patterns('',
	    (r'^[whatever_you_want]/', include('chiplog.urls')),

Add a symbolic link to the Chiplog media folder inside your project's media folder. Something like:

	cd /path/to/your/project/media
	ln -s /path/to/chiplog/static chiplog
