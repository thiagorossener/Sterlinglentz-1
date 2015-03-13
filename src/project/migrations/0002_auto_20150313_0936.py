# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttext',
            name='projectcontent_ptr',
        ),
        migrations.DeleteModel(
            name='ProjectText',
        ),
        migrations.AlterModelOptions(
            name='projectcontent',
            options={'ordering': ['ordering'], 'verbose_name': 'Project Content', 'verbose_name_plural': 'Project Content'},
        ),
    ]
