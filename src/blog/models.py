from django.db import models


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
    image = models.ImageField(blank=True, null=True, upload_to='blog/')

    slug = models.SlugField(unique=True)

    meta_title = models.CharField(blank=True, null=True, max_length=80,
        help_text=""" Meta title should be between 50-60 chars (80 max)""")
    meta_description = models.TextField(blank=True, null=True, max_length=115,
        help_text=""" Meta title should be around 115 chars (130 max)""")

    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["edited_on"]
        get_latest_by = "created_on"

    def __unicode__(self):
        return "{}".format(self.title)
