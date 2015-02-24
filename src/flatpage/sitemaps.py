from django.contrib.sitemaps import Sitemap

from .models import FlatPage


class FlatPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return FlatPage.published.all()

    def lastmod(self, obj):
        return obj.edited_on
