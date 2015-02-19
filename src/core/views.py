""" Basic views. """

from django.views.generic import TemplateView

from content.views import BlockMixin


class IndexView(BlockMixin, TemplateView):

    """ The homepage view. """

    template_name = "index.html"
    block_identifier = "pages.index"


class StudioView(BlockMixin, TemplateView):

    """ The studio view. """

    template_name = "studio.html"
    block_identifier = "pages.studio"
