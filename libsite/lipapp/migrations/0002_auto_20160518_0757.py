# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lipapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lipapp.Libitem')),
                ('author', models.CharField(max_length=100)),
                ('category', models.IntegerField(choices=[(1, 'Fiction'), (2, 'Biography'), (3, 'Self Help'), (4, 'Education'), (5, 'Children'), (6, 'Teen'), (7, 'Other')], default=1)),
            ],
            bases=('lipapp.libitem',),
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lipapp.Libitem')),
                ('maker', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
            ],
            bases=('lipapp.libitem',),
        ),
        migrations.RemoveField(
            model_name='libuser',
            name='age',
        ),
        migrations.AddField(
            model_name='libitem',
            name='num_chkout',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='libuser',
            name='postalcode',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]