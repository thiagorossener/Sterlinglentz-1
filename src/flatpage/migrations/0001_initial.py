# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100, verbose_name=b'URL', db_index=True)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(help_text=b'\n        * Dependant on template', max_length=200, blank=True)),
                ('subsubtitle', models.CharField(help_text=b'\n        * Dependant on template', max_length=200, blank=True)),
                ('description', models.TextField(blank=True)),
                ('image_caption', models.CharField(max_length=200, null=True, blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('sidebar', ckeditor.fields.RichTextField()),
                ('template_name', models.CharField(default=b'flatpage/basic.html', max_length=70, blank=True, choices=[(b'flatpage/alpha.html', b'Basic Template (Alpha Layout)'), (b'flatpage/beta.html', b'Advanced Template (Beta Layout)')])),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('menu_title', models.CharField(max_length=70, blank=True)),
                ('meta_title', models.CharField(help_text=b' Meta title should be between 50-60 chars (80 max)', max_length=80, null=True, blank=True)),
                ('meta_description', models.TextField(help_text=b' Meta title should be around 115 chars (130 max)', max_length=115, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('image', filer.fields.image.FilerImageField(related_name='flatpage_landscape_image', blank=True, to='filer.Image', help_text=b'Should be around 1600x500 pixels  (or similar aspect)', null=True)),
                ('menu_node', models.ForeignKey(blank=True, to='menu.MenuNode', null=True)),
            ],
            options={
                'ordering': ('ordering',),
                'db_table': 'django_flatpage',
                'verbose_name': 'flat page',
                'verbose_name_plural': 'flat pages',
            },
            bases=(models.Model,),
        ),
    ]
