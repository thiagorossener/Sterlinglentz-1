from django.views.generic import TemplateView
from django.http import Http404

from blog.models import Post
from core.mixins import AjaxPartialRenderingMixin


class BlogMixin(object):

    """ A mixin with common functionality. """

    all_posts = None
    display_post = None

    def dispatch(self, request, *args, **kwargs):
        """ Retrieve the blog posts. """
        self.all_posts = self.get_all_posts()
        self.display_post = self.get_display_post()
        return super(BlogMixin, self).dispatch(request, *args, **kwargs)

    def get_all_posts(self):
        """ Retrieve all blog posts. """
        return Post.published.all()

    def get_display_post(self):
        """ Get the blog posts that is to be displayed. """
        if not self.all_posts:
            return None
        return self.all_posts.latest()

    def get_context_data(self, **kwargs):
        """ Add posts to the context. """
        context = super(BlogMixin, self).get_context_data(**kwargs)
        context.update({
            'all_posts': self.all_posts,
            'display_post': self.display_post
        })
        return context


class BlogDetailView(AjaxPartialRenderingMixin, BlogMixin, TemplateView):

    template_name = "blog.html"
    partial_template_name = "blog--partial.html"

    def get_display_post(self):
        """ Get the blog posts that is to be displayed. """
        try:
            return self.all_posts.get(slug=self.kwargs['slug'])
        except Post.DoesNotExist:
            raise Http404


class BlogLatestView(AjaxPartialRenderingMixin, BlogMixin, TemplateView):

    """ """

    template_name = "blog.html"
    partial_template_name = "blog--partial.html"
