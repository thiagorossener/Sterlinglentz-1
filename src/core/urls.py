from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, StudioView


urlpatterns = patterns(
    '',
    url(r'^studio/$', StudioView.as_view(), name="studio"),
    url(r'^$', IndexView.as_view(), name="index"),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
