# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20150219_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='content',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=True,
        ),
    ]
