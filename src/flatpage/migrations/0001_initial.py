# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=100, verbose_name='URL', db_index=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('subtitle', models.CharField(max_length=200, verbose_name='subtitle', blank=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('template_name', models.CharField(help_text="Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'.", max_length=70, verbose_name='template name', blank=True)),
                ('landscape_image', filer.fields.image.FilerImageField(related_name='flatpage_landscape_image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'ordering': ('url',),
                'db_table': 'django_flatpage',
                'verbose_name': 'flat page',
                'verbose_name_plural': 'flat pages',
            },
            bases=(models.Model,),
        ),
    ]
