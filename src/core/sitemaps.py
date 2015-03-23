from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['index', ]

    def location(self, item):
        return reverse(item)
