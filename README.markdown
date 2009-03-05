**Chiplog** is a simple way to enter notes that get time/date stamped. It's a way to document what you're doing without having to deal with how to manage it. It's written in Django.

Inspired by Cliff Stoll's Log Book in [Cuckoo's Egg](http://readernaut.com/trey/notes/68/).

The name is taking things back to [where the word "Log" came from in the first place](http://en.wikipedia.org/wiki/Chip_log).

Requirements

- [Django Tagging](http://code.google.com/p/django-tagging/)
- [Django Markup](http://docs.djangoproject.com/en/dev/ref/contrib/#markup) (django.contrib.markup)
- [Django Humanize](http://docs.djangoproject.com/en/dev/ref/contrib/humanize/) (django.contrib.humanize)
- [Python Markdown](http://err.no/pymarkdown/pymarkdown.py)
- [Typogrify](http://typogrify.googlecode.com/)

---

**Installation**

In `settings.py`, add to `INSTALLED_APPS`:

	'chiplog',
	'tagging',
	'typogrify',
	'django.contrib.markup',
	'django.contrib.humanize',

Also in `settings.py`, add the following setting:

	CHIPLOG_MEDIA_URL = MEDIA_URL + 'chiplog/'

And add at the context processor of chiplog:

    TEMPLATE_CONTEXT_PROCESSORS = (
        'chiplog.context_processors.chiplog_media_url',
        ...
    )

In `urls.py`:

	urlpatterns = patterns('',
	    (r'^[whatever_you_want]/', include('chiplog.urls')),

Add a symbolic link to the Chiplog media folder inside your project's media folder. Something like:

	cd /path/to/your/project/media
	ln -s /path/to/chiplog/static chiplog

Run `./manage.py syncdb` from the root of your project, and you should be ready to start Chiplogging.

---

**Optional**

If you don't already have something configured, you can add a login template from [the example Chiplog project](http://github.com/trey/chiplog_proj).

Copy [`templates/registration/`](http://github.com/trey/chiplog_proj/tree/master/templates/registration) to your project's template folder.

Add to `urls.py`:

	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
