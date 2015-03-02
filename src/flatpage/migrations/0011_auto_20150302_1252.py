# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpage', '0010_auto_20150302_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='subsubtitle',
            field=models.CharField(help_text=b'\n        * Dependant on template', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='subtitle',
            field=models.CharField(help_text=b'\n        * Dependant on template', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='template_name',
            field=models.CharField(blank=True, max_length=70, choices=[(b'flatpage/basic.html', b'Basic Template'), (b'flatpage/advanced.html', b'Advanced Template')]),
            preserve_default=True,
        ),
    ]
