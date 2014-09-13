# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='odPairs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.CharField(max_length=25, db_index=True)),
                ('destination', models.CharField(max_length=25, db_index=True)),
                ('ttime', models.FloatField(db_index=True)),
                ('tdist', models.FloatField(db_index=True)),
                ('mode', models.ForeignKey(to='od_api.modes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
