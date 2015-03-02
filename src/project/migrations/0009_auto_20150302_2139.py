# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_projectimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimage',
            options={'ordering': ['ordering'], 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.RenameField(
            model_name='projectimage',
            old_name='order',
            new_name='ordering',
        ),
    ]
