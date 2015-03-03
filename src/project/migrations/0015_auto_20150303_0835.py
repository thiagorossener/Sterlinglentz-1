# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20150303_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='alt_text',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='title_text',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
