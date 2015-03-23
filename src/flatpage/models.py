from django.db import models
from django.core.urlresolvers import get_script_prefix
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import iri_to_uri

from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


TEMPLATE_CHOICES = (
    ('flatpage/alpha.html', 'Basic Template (Alpha Layout)'),
    ('flatpage/beta.html', 'Advanced Template (Beta Layout)'),
)


class PublishedFlatPageManager(models.Manager):

    """ A manager to return only published flatpage. """

    def get_queryset(self):
        return super(PublishedFlatPageManager, self).get_queryset() \
            .filter(is_published=True)


class FlatPage(models.Model):

    """ A custom flatpage model based on django.contrib.flatpages. """

    objects = models.Manager()
    published = PublishedFlatPageManager()

    url = models.CharField('URL', max_length=100, db_index=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, help_text="""
        * Dependant on template""")
    subsubtitle = models.CharField(max_length=200, blank=True, help_text="""
        * Dependant on template""")
    description = models.TextField(blank=True)

    image = FilerImageField(null=True, blank=True,
        related_name="flatpage_landscape_image", help_text="Should be around 1600x500 pixels  (or similar aspect)")
    image_caption = models.CharField(max_length=200, null=True, blank=True)

    content = RichTextField()
    sidebar = RichTextField()

    template_name = models.CharField(max_length=70, blank=True,
        choices=TEMPLATE_CHOICES, default="flatpage/basic.html")
    menu_node = models.ForeignKey("menu.MenuNode", blank=True, null=True)
    ordering = models.PositiveIntegerField(default=0)
    menu_title = models.CharField(max_length=70, blank=True)
    meta_title = models.CharField(blank=True, null=True, max_length=80,
        help_text=""" Meta title should be between 50-60 chars (80 max)""")
    meta_description = models.TextField(blank=True, null=True, max_length=115,
        help_text=""" Meta title should be around 115 chars (130 max)""")

    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'django_flatpage'
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('ordering',)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.menu_title = self.title
            self.meta_title = self.title
            self.meta_description = self.description
        return super(FlatPage, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
