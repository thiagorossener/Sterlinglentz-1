# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150603_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='index_action_text',
            new_name='action_text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='index_color',
        ),
        migrations.AddField(
            model_name='project',
            name='primary_color',
            field=models.CharField(default=b'000000', help_text=b'The primary hex color associated with this project', max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='secondary_color',
            field=models.CharField(default=b'ffffff', help_text=b'The secondary hex color associated with this project', max_length=6),
            preserve_default=True,
        ),
    ]
