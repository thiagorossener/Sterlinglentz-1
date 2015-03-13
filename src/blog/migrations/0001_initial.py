# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('subtitle', models.CharField(max_length=512, null=True, blank=True)),
                ('extract', models.TextField(null=True, blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(unique=True)),
                ('meta_title', models.CharField(help_text=b' Meta title should be between 50-60 chars (80 max)', max_length=80, null=True, blank=True)),
                ('meta_description', models.TextField(help_text=b' Meta title should be around 115 chars (130 max)', max_length=115, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('image', filer.fields.image.FilerImageField(related_name='post_image', blank=True, to='filer.Image', help_text=b'Should be around 1600x500 pixels  (or similar aspect)', null=True)),
            ],
            options={
                'ordering': ['edited_on'],
                'get_latest_by': 'created_on',
            },
            bases=(models.Model,),
        ),
    ]
