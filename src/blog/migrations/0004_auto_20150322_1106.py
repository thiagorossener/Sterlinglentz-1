# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150319_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'get_latest_by': 'created_on'},
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
