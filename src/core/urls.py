from django.conf.urls import patterns, url

from .views import IndexView, StudioView


urlpatterns = patterns(
    '',
    url(r'^studio/$', StudioView.as_view(), name="studio"),
    url(r'^$', IndexView.as_view(), name="index"),
)
