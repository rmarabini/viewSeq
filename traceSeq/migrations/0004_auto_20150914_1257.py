# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceSeq', '0003_seq_seqname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seq',
            name='state',
            field=models.CommaSeparatedIntegerField(max_length=32000),
        ),
    ]
