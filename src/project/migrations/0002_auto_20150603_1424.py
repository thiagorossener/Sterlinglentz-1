# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='index_action_text',
            field=models.CharField(default=' ', help_text=b"e.g. 'Designing a website for'", max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='index_color',
            field=models.CharField(default=b'ffffff', help_text=b'The hex color associated with this project', max_length=6),
            preserve_default=True,
        ),
    ]
