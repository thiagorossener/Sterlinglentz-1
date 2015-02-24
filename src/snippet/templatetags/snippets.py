from django import template
from django.utils.safestring import mark_safe

register = template.Library()

from snippet.models import Snippet


@register.simple_tag(takes_context=True)
def snippet(context, slug):
    snippet = None
    try:
        snippet = Snippet.objects.get(slug=slug)
    except Snippet.DoesNotExist:
        pass
    return mark_safe(snippet.content)