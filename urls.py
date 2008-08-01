from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^logbook/', include('logbook.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)

# This allows Django to serve static files when you're developing your project.
# You'll have to do something else in production.
# More information: http://www.djangoproject.com/documentation/static_files/
# -----------------------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += patterns("django.views",
        url(r"^static/(?P<path>.*)", "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
