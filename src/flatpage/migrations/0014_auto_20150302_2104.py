# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0013_remove_flatpage_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='in_navigation',
        ),
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
            name='rght',
        ),
        migrations.RemoveField(
            model_name='flatpage',
            name='tree_id',
        ),
    ]
