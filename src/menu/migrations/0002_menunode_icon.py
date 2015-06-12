# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menunode',
            name='icon',
            field=filer.fields.image.FilerImageField(related_name='menunode_icon', blank=True, to='filer.Image', help_text=b'Should be around 32x32 pixels', null=True),
            preserve_default=True,
        ),
    ]
