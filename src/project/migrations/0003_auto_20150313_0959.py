# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150313_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectvideo',
            name='source',
        ),
        migrations.AddField(
            model_name='projectvideo',
            name='html',
            field=models.TextField(default='', help_text=b'The HTML outputted by SublimeVideo website'),
            preserve_default=False,
        ),
    ]
