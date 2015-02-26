""" Custom global context processors. """

from .models import FlatPage


def flatpages(object):
    return {
        "flatpages": FlatPage.published.filter(in_navigation=True)
    }
