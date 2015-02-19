from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^admin-dashboard/', include(admin.site.urls)),

    url(r'^', include("core.urls")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
