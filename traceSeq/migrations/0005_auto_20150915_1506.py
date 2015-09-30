# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceSeq', '0004_auto_20150914_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='struct',
            name='seq',
        ),
        migrations.AddField(
            model_name='seq',
            name='struct',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='seq',
            name='state',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Struct',
        ),
    ]
