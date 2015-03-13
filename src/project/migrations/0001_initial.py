# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['ordering', 'name'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('focus', models.CharField(max_length=128)),
                ('homepage', models.URLField(blank=True)),
                ('ordering', models.PositiveIntegerField(default=0, help_text=b' ')),
                ('slug', models.SlugField(unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['ordering', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('meta_title', models.CharField(help_text=b' Meta title should be between 50-60 chars (80 max)', max_length=80, null=True, blank=True)),
                ('meta_description', models.TextField(help_text=b' Meta title should be around 115 chars (130 max)', max_length=115, null=True, blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='project.Category')),
                ('client', models.ForeignKey(to='project.Client')),
                ('landscape_image', filer.fields.image.FilerImageField(related_name='project_landscape_image', blank=True, to='filer.Image', help_text=b'Should be around 1600x500 pixels  (or similar aspect)', null=True)),
                ('portrait_image', filer.fields.image.FilerImageField(related_name='project_listing_image', blank=True, to='filer.Image', help_text=b'Should be around 600x800 pixels (or similar aspect)', null=True)),
            ],
            options={
                'ordering': ['ordering', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.PositiveIntegerField(default=0, null=True, blank=True)),
            ],
            options={
                'ordering': ['ordering'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('projectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='project.ProjectContent')),
                ('caption', models.CharField(max_length=256, blank=True)),
                ('title_text', models.CharField(max_length=256, blank=True)),
                ('alt_text', models.CharField(max_length=256, blank=True)),
                ('width', models.IntegerField(default=100, help_text=b'A percentage between 0 and 100', verbose_name=b'Width')),
                ('x_offset', models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image by horizontally', verbose_name=b'Horizontal Offset')),
                ('y_offset', models.IntegerField(default=0, help_text=b'Number of pixels (positive or negative) to offset the image by vertically', verbose_name=b'Vertical Offset')),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
            bases=('project.projectcontent',),
        ),
        migrations.CreateModel(
            name='ProjectText',
            fields=[
                ('projectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='project.ProjectContent')),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Text',
            },
            bases=('project.projectcontent',),
        ),
        migrations.CreateModel(
            name='ProjectVideo',
            fields=[
                ('projectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='project.ProjectContent')),
                ('source', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
            bases=('project.projectcontent',),
        ),
        migrations.AddField(
            model_name='projectcontent',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_project.projectcontent_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectcontent',
            name='project',
            field=models.ForeignKey(related_name='content_items', to='project.Project'),
            preserve_default=True,
        ),
    ]
