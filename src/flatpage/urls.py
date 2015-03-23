from django.conf.urls import patterns, url

from flatpage.views import FlatpageView


urlpatterns = patterns(
    '',
    url(r'^(?P<url>.*)$', FlatpageView.as_view()),
)
