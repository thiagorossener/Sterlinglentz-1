""" Basic views. """

from django.views.generic import TemplateView


class IndexView(TemplateView):

    """ The homepage view. """

    template_name = "index.html"
