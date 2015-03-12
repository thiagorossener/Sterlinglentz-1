from django.views.generic import DetailView, ListView

from blog.models import Post
from core.mixins import AjaxPartialRenderingMixin


class BlogDetailView(AjaxPartialRenderingMixin, DetailView):

    template_name = "blog/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.published.all()


class BlogListView(AjaxPartialRenderingMixin, ListView):

    """ """

    template_name = "blog/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.published.all()
