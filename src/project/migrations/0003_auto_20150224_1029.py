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
            name='meta_description',
            field=models.TextField(help_text=b' Meta title should be around 115 chars (130 max)', max_length=115, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='meta_title',
            field=models.CharField(help_text=b' Meta title should be between 50-60 chars (80 max)', max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
    ]
