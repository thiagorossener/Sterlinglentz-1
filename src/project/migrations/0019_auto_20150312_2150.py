# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20150312_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='x_offset',
            field=models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image by horizontally', verbose_name=b'Horizontal Offset'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='y_offset',
            field=models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image by vertically', verbose_name=b'Vertical Offset'),
            preserve_default=True,
        ),
    ]
