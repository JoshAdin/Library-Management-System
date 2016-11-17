# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 20:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipapp', '0005_auto_20160617_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='libitem',
            name='date_acquired',
            field=models.DateField(default=datetime.date(2016, 6, 18)),
        ),
    ]
