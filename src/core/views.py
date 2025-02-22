""" Basic views. """

from django.views.generic import TemplateView

from project.models import Project
from blog.models import Post
from core.mixins import AjaxPartialRenderingMixin


class IndexView(AjaxPartialRenderingMixin, TemplateView):

    """ The homepage view. """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        projects = None
        try:
            projects = Project.published.all()[:4]
        except Project.DoesNotExist:
            pass

        post = None
        try:
            post = Post.published.latest()
        except Post.DoesNotExist:
            pass

        context.update({
            'projects': projects,
            'post': post
        })
        return context
