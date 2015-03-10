# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20150303_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='caption',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
