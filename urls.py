from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^logbook_django/', include('logbook_django.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
