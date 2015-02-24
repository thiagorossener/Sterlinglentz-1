""" Feral Projects """

from django.db import models

from ckeditor.fields import RichTextField


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


class PublishedManager(models.Manager):

    """ A manager to return only published projects. """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset() \
            .filter(is_published=True)


class Project(models.Model):

    """ A single project belonging to a client. """

    published = PublishedManager()

    client = models.ForeignKey(Client)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    homepage = models.URLField(blank=True)
    categories = models.ManyToManyField(Category)

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

    def __unicode__(self):
        return "{} by {}".format(self.name, self.client.name)
