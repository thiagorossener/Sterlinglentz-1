# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=cms.models.fields.PlaceholderField(slotname=b'content', editable=False, to='cms.Placeholder', null=True),
            preserve_default=True,
        ),
    ]
