# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='post_image', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
