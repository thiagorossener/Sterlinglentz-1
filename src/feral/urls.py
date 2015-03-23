from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

from blog.sitemaps import PostSitemap
from project.sitemaps import ProjectSitemap
from flatpage.sitemaps import FlatPageSitemap
from core.sitemaps import StaticSitemap


SITEMAPS = {
    'posts': PostSitemap,
    'projects': ProjectSitemap,
    'pages': FlatPageSitemap,
    'static': StaticSitemap
}

urlpatterns = patterns(
    '',
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    url(r'^google8c62f7d46e66f32e.html$', lambda r: HttpResponse("google-site-verification: google8c62f7d46e66f32e.html", content_type="text/plain")),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': SITEMAPS}),

    url(r'^admin-dashboard/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^projects/', include("project.urls", namespace="projects")),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^', include("core.urls")),
    url(r'^', include('flatpage.urls', namespace="flatpages")),
)

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT) + \
                  urlpatterns
