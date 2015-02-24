# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('project', '0003_auto_20150224_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='headline_image',
            field=filer.fields.image.FilerImageField(related_name='project_headline_image', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='listing_image',
            field=filer.fields.image.FilerImageField(related_name='project_listing_image', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
