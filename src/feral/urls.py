from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^admin-dashboard/', include(admin.site.urls)),

    url(r'^projects/', include("project.urls", namespace="projects")),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^', include("core.urls")),
)
