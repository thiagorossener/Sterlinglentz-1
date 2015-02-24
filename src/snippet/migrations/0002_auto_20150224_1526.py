# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=models.CharField(help_text=b'An optional description for internal use only', max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
    ]
