# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-10 15:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190809_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='Data',
            field=models.DateField(default=datetime.datetime(2019, 8, 10, 15, 5, 17, 633155, tzinfo=utc)),
        ),
    ]
