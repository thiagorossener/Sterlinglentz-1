# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_project_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='landscape_image',
            field=filer.fields.image.FilerImageField(related_name='project_landscape_image', blank=True, to='filer.Image', help_text=b'Should be around 1600x500 pixels  (or similar aspect)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='portrait_image',
            field=filer.fields.image.FilerImageField(related_name='project_listing_image', blank=True, to='filer.Image', help_text=b'Should be around 600x800 pixels (or similar aspect)', null=True),
            preserve_default=True,
        ),
    ]
