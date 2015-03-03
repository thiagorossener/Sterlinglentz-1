# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150302_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menunode',
            options={'verbose_name': 'Menu Node', 'verbose_name_plural': 'Menu Nodes'},
        ),
        migrations.AddField(
            model_name='menunode',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
