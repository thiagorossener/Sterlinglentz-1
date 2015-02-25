# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('blog', '0004_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='post_image', blank=True, to='filer.Image', help_text=b'Should be around 1600x500 pixels  (or similar aspect)', null=True),
            preserve_default=True,
        ),
    ]
