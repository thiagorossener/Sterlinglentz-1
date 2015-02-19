# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150219_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='json',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='block',
            name='json',
        ),
        migrations.AddField(
            model_name='block',
            name='content',
            field=jsonfield.fields.JSONField(default=b'{}'),
            preserve_default=True,
        ),
    ]
