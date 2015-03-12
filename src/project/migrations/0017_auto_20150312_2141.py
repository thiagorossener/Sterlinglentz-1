# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_projectimage_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='image_width',
            field=models.IntegerField(default=100, help_text=b'A percentage between 0 and 100'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='image_xoffset',
            field=models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image horizontally'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='image_yoffset',
            field=models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image vertically'),
            preserve_default=True,
        ),
    ]
