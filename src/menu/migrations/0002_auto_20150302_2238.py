# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menunode',
            options={'ordering': ('ordering',), 'verbose_name': 'Menu Node', 'verbose_name_plural': 'Menu Nodes'},
        ),
    ]
