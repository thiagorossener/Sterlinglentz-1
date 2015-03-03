# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0015_auto_20150302_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='level',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='tree_id',
        ),
    ]
