from django.contrib.sitemaps import Sitemap

from .models import Project


class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Project.published.all()

    def lastmod(self, obj):
        return obj.edited_on
