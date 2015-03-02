# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0012_auto_20150302_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='parent',
        ),
    ]
