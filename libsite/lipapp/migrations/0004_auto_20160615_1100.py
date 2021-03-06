# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 15:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipapp', '0003_auto_20160525_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubyr', models.IntegerField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Book'), (2, 'DVD'), (3, 'Other')], default=1)),
                ('cost', models.IntegerField()),
                ('num_interested', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='dvd',
            name='rating',
            field=models.CharField(blank=True, choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('14A', '14A'), ('R', 'R'), ('NR', 'NR')], max_length=10),
        ),
        migrations.AlterField(
            model_name='libitem',
            name='date_acquired',
            field=models.DateField(default=datetime.date(2016, 6, 15)),
        ),
    ]
