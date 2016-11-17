# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 00:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipapp', '0004_auto_20160615_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libitem',
            name='date_acquired',
            field=models.DateField(default=datetime.date(2016, 6, 17)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]