# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=100, verbose_name=b'URL', db_index=True)),
                ('is_published', models.BooleanField(default=True)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='menu.MenuNode', null=True)),
            ],
            options={
                'verbose_name': 'Menu Node',
                'verbose_name_plural': 'Menu Nodes',
            },
            bases=(models.Model,),
        ),
    ]
