# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20150224_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='homepage',
        ),
    ]
