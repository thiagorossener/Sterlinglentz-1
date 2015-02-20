from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^admin-dashboard/', include(admin.site.urls)),

    url(r'^projects/', include("project.urls", namespace="projects")),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^', include("core.urls")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
