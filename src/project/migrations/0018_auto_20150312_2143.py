# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20150312_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='image_width',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='image_xoffset',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='image_yoffset',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='width',
            field=models.IntegerField(default=100, help_text=b'A percentage between 0 and 100', verbose_name=b'Width'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='x_offset',
            field=models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image horizontally', verbose_name=b'Horizontal Offset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='y_offset',
            field=models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image vertically', verbose_name=b'Vertical Offset'),
            preserve_default=True,
        ),
    ]
