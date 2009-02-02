from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
@stringfilter
def autolink(value):
    """
    Create anchor tags for URLs that aren't already in anchor tags.
    """
    return re.sub(r'[^(href=")](http|https|ftp)(:\/\/[^\s]*)', r'<a href="\1\2">\1\2</a>', value)
autolink.is_safe = True
