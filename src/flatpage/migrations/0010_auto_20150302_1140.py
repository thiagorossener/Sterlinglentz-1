# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0009_flatpage_in_navigation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flatpage',
            options={'ordering': ('ordering',), 'verbose_name': 'flat page', 'verbose_name_plural': 'flat pages'},
        ),
        migrations.AddField(
            model_name='flatpage',
            name='menu_title',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='subsubtitle',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='subtitle',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
