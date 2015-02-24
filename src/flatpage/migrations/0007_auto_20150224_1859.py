# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0006_flatpage_sidebar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='flatpage_landscape_image', blank=True, to='filer.Image', help_text='Should be 1200x400', null=True),
            preserve_default=True,
        ),
    ]
