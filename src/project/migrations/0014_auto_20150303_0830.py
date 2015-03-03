# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20150303_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(related_name='images', to='project.Project'),
            preserve_default=True,
        ),
    ]
