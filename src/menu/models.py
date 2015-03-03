from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from mptt.managers import TreeManager


class MenuNode(MPTTModel):
    objects = TreeManager()

    name = models.CharField(max_length=200)
    url = models.CharField('URL', max_length=100, db_index=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children')

    is_published = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['ordering']

    class Meta:
        verbose_name = "Menu Node"
        verbose_name_plural = "Menu Nodes"

    def save(self, *args, **kwargs):
        super(MenuNode, self).save(*args, **kwargs)
        MenuNode.objects.rebuild()

    def __unicode__(self):
        return "{0.name} -- {0.url}".format(self)
