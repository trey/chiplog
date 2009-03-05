# -*- coding: utf-8 -*-

def chiplog_media_url(request):
    '''Makes the CHIPLOG_MEDIA_URL setting available to all templates.'''
    from django.conf import settings
    return {'chiplog_media_url': settings.CHIPLOG_MEDIA_URL}