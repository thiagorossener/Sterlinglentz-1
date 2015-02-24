# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='flatpage',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='template_name',
            field=models.CharField(max_length=70, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
