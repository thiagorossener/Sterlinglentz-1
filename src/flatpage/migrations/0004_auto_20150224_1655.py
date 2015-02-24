# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0003_auto_20150224_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flatpage',
            old_name='landscape_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
