from django.conf.urls import patterns, url

from .views import ProjectListView, ProjectDetailView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(),
        name='detail'),
    url(r'^$', ProjectListView.as_view(), name='list'),
)
