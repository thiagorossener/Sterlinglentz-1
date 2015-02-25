# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0007_auto_20150224_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='flatpage_landscape_image', blank=True, to='filer.Image', help_text=b'Should be around 1600x500 pixels  (or similar aspect)', null=True),
            preserve_default=True,
        ),
    ]
