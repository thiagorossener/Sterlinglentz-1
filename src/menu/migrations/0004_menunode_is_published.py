# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20150303_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='menunode',
            name='is_published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
