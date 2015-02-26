# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0008_auto_20150225_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='in_navigation',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
