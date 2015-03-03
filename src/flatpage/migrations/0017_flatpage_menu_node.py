# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150302_2238'),
        ('flatpage', '0016_auto_20150302_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='menu_node',
            field=models.ForeignKey(blank=True, to='menu.MenuNode', null=True),
            preserve_default=True,
        ),
    ]
