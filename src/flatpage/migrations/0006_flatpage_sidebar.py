# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0005_auto_20150224_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='sidebar',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
