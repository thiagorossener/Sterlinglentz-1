""" Models related to content. """

from django.db import models

from jsonfield import JSONField


class Template(models.Model):

    """ This is a template that can be used to populate a particular block. """

    title = models.CharField(max_length=50)
    content = JSONField()

    def __unicode__(self):
        return self.title


class Block(models.Model):

    """ A basic piece of content used throughout the site. """

    identifier = models.CharField(max_length=128, unique=True, help_text="""A
        unique, dotted identified for this content block.
        e.g 'global.config'""")
    description = models.CharField(
        blank=True, max_length=128, help_text="""For your own internal
        use only""")
    identifier = models.CharField(max_length=128)

    content = JSONField(default={})

    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["identifier"]
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    def __unicode__(self):
        return self.identifier
