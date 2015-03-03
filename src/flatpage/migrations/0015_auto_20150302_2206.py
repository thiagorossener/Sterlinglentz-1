# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0014_auto_20150302_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='flatpage.FlatPage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flatpage',
            name='tree_id',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
