from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class PostManager(models.Manager):

    """ A manager to return only published posts. """

    def get_queryset(self):
        return super(PostManager, self).get_queryset() \
            .filter(is_published=True)


class Post(models.Model):

    """ A blog post. """

    published = PostManager()

    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512, blank=True, null=True)
    extract = models.TextField(blank=True, null=True)

    image = FilerImageField(null=True, blank=True, related_name="post_image",
        help_text="Should be around 1600x500 pixels  (or similar aspect)")

    content = RichTextField()

    slug = models.SlugField(unique=True)

    meta_title = models.CharField(blank=True, null=True, max_length=80,
        help_text=""" Meta title should be between 50-60 chars (80 max)""")
    meta_description = models.TextField(blank=True, null=True, max_length=115,
        help_text=""" Meta title should be around 115 chars (130 max)""")

    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        get_latest_by = "created_on"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.meta_title = self.title
            self.meta_description = self.subtitle
        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={
            'slug': self.slug
        })
