# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(help_text=b'For your own internal\n        use only', blank=True)),
                ('identifier', models.CharField(max_length=128)),
                ('json', jsonfield.fields.JSONField()),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['identifier'],
            },
            bases=(models.Model,),
        ),
    ]
