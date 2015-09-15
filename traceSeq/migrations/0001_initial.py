# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.TextField()),
                ('state', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Struct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('init', models.IntegerField()),
                ('finish', models.IntegerField()),
                ('type', models.IntegerField()),
                ('seq', models.ForeignKey(to='traceSeq.Seq')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='seq',
            field=models.ForeignKey(to='traceSeq.Seq'),
        ),
    ]
