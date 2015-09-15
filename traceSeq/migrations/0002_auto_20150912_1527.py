# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceSeq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='struct',
            name='type',
            field=models.CharField(max_length=12),
        ),
    ]
