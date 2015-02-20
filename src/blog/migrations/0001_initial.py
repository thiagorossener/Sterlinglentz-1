# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('subtitle', models.CharField(max_length=512, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'blog/', blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('meta_title', models.CharField(help_text=b' Meta title should be between 50-60 chars (80 max)', max_length=80, null=True, blank=True)),
                ('meta_description', models.TextField(help_text=b' Meta title should be around 115 chars (130 max)', max_length=115, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['edited_on'],
            },
            bases=(models.Model,),
        ),
    ]
