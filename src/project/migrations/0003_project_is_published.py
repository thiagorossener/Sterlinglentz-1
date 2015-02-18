# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
