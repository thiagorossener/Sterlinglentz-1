# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('project', '0004_auto_20150224_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='listing_image',
            new_name='portrait_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='headline_image',
        ),
        migrations.AddField(
            model_name='project',
            name='landscape_image',
            field=filer.fields.image.FilerImageField(related_name='project_landscape_image', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
