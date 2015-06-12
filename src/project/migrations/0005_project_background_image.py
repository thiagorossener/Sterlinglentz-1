# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('project', '0004_auto_20150603_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='background_image',
            field=filer.fields.image.FilerImageField(related_name='project_background_image', blank=True, to='filer.Image', help_text=b'Should be around 900x750 pixels (or similar aspect)', null=True),
            preserve_default=True,
        ),
    ]
