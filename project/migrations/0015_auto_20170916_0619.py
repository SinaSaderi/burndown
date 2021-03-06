# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-16 06:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20170916_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closeddays',
            name='day',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Closed day'),
        ),
        migrations.AlterField(
            model_name='hours',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start date'),
        ),
    ]
