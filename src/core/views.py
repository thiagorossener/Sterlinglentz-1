""" Basic views. """

from django.views.generic import TemplateView

from content.views import BlockMixin
from project.models import Project
from blog.models import Post


class IndexView(BlockMixin, TemplateView):

    """ The homepage view. """

    template_name = "index.html"
    block_identifier = "pages.index"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'projects': Project.published.all()[:3],
            'post': Post.published.latest()
        })
        return context


class StudioView(BlockMixin, TemplateView):

    """ The studio view. """

    template_name = "studio.html"
    block_identifier = "pages.studio"
