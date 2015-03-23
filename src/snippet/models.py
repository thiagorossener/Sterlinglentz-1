from django.db import models


class Snippet(models.Model):

    """ """

    slug = models.CharField(unique=True, max_length=256, help_text="""
        Should be a dot-seprated string""")
    description = models.CharField(blank=True, null=True, max_length=128,
        help_text="""An optional description for internal use only""")
    content = models.TextField()

    def __unicode__(self):
        return self.slug
