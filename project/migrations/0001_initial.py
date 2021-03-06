# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 10:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start date')),
                ('dead_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Dead date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]
