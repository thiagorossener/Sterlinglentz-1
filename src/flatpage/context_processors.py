""" Custom global context processors. """

from flatpage.models import FlatPage


def flatpages(object):
    return {
        "flatpages": FlatPage.published.filter()
    }
