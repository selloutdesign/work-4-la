# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20170723_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='exam_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_high',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_low',
            field=models.IntegerField(blank=True),
        ),
    ]
