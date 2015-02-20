from django.conf.urls import patterns, url

from .views import BlogLatestView, BlogDetailView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', BlogDetailView.as_view(), name='detail'),
    url(r'^$', BlogLatestView.as_view(), name='latest'),
)
