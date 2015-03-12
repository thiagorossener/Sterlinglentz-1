# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='extract',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
