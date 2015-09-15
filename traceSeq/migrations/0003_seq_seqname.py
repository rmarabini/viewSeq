# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceSeq', '0002_auto_20150912_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='seq',
            name='seqName',
            field=models.CharField(default=b'noname', max_length=64),
        ),
    ]
