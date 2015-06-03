# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150603_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='primary_color',
            new_name='color',
        ),
        migrations.RemoveField(
            model_name='project',
            name='secondary_color',
        ),
    ]
