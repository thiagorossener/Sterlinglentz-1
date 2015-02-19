""" Models related to content. """

from django.db import models

from jsonfield import JSONField


class ContentBlock(models.Model):

    """ A basic piece of content used throughout the site. """

    identifier = models.CharField(max_length=128, unique=True, help_text="""A
        unique, dotted identified for this content block.
        e.g 'global.config'""")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, help_text="""For your own internal
        use only""")
    identifier = models.CharField(max_length=128)

    json = JSONField()

    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["identifier"]
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    def __unicode__(self):
        return self.identifier
