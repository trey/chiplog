from django.conf import settings

CHIPLOG_MEDIA_URL = getattr(settings, 'CHIPLOG_MEDIA_URL', settings.MEDIA_URL + 'chiplog/')
