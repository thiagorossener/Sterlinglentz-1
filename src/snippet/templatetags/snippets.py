from django import template

register = template.Library()

from snippet.models import Snippet


@register.simple_tag
def snippet(slug):
    snippet = None
    try:
        snippet = Snippet.objects.get(slug=slug)
    except Snippet.DoesNotExist:
        pass
    return snippet.content