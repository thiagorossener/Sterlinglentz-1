from django.conf.urls import patterns, url

from .views import BlogListView, BlogDetailView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', BlogDetailView.as_view(), name='detail'),
    url(r'^$', BlogListView.as_view(), name='list'),
)
