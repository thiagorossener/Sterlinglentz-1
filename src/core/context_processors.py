""" Custom global context processors. """

from content.models import Block


def menu(object):
    """ Insert our menu block content into every template. """
    block, created = Block.objects.get_or_create(
        identifier="global.menu_items")
    if created:
        block.json = []
        block.save()
    return {
        "menu": block.json
    }
