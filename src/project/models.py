""" Feral Projects """

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class Client(models.Model):

    """ A client a project was completed for. """

    name = models.CharField(max_length=128)
    focus = models.CharField(max_length=128)
    homepage = models.URLField(blank=True)

    ordering = models.PositiveIntegerField(default=0, help_text=""" """)
    slug = models.SlugField(unique=True)

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordering", "name"]

    def __unicode__(self):
        return self.name


class Category(models.Model):

    """ A project category such as 'Product Design'. """

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    ordering = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordering", "name"]
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class ProjectImage(models.Model):

    """ An image for a particular project. """

    project = models.ForeignKey("Project", related_name="images")
    image = FilerImageField(null=True, blank=True)
    caption = models.CharField(max_length=256, blank=True)
    title_text = models.CharField(max_length=256, blank=True)
    alt_text = models.CharField(max_length=256, blank=True)
    ordering = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["ordering", ]
        verbose_name = "Image"
        verbose_name_plural = "Images"


class PublishedManager(models.Manager):

    """ A manager to return only published projects. """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
            .filter(is_published=True)


class Project(models.Model):

    """ A single project belonging to a client. """

    published = PublishedManager()
    objects = models.Manager()

    client = models.ForeignKey(Client)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)

    landscape_image = FilerImageField(null=True, blank=True,
        related_name="project_landscape_image", help_text="Should be around 1600x500 pixels  (or similar aspect)")
    portrait_image = FilerImageField(null=True, blank=True,
        related_name="project_listing_image", help_text="Should be around 600x800 pixels (or similar aspect)")

    content = RichTextField()

    ordering = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)

    meta_title = models.CharField(blank=True, null=True, max_length=80,
        help_text=""" Meta title should be between 50-60 chars (80 max)""")
    meta_description = models.TextField(blank=True, null=True, max_length=115,
        help_text=""" Meta title should be around 115 chars (130 max)""")

    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordering", "name"]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.meta_title = self.name
            self.meta_description = self.description
        return super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{} by {}".format(self.name, self.client.name)

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={
            'slug': self.slug
        })
