# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-08 16:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_contato_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='Data',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 8, 8, 16, 39, 15, 577309)),
        ),
    ]
