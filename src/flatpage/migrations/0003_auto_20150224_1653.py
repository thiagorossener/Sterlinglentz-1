# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0002_auto_20150224_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 16, 53, 20, 144995), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='edited_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 16, 53, 25, 162196), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='is_published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='meta_description',
            field=models.TextField(help_text=' Meta title should be around 115 chars (130 max)', max_length=115, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='meta_title',
            field=models.CharField(help_text=' Meta title should be between 50-60 chars (80 max)', max_length=80, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='ordering',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
