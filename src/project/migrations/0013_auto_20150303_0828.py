# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20150302_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='images', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
