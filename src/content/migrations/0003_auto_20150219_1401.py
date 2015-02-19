# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20150219_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='title',
        ),
        migrations.AlterField(
            model_name='block',
            name='description',
            field=models.CharField(help_text=b'For your own internal\n        use only', max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
