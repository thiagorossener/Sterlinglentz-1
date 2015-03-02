# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20150302_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='ordering',
            field=models.PositiveIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
