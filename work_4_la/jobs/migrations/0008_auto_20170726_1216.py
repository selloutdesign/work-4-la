# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20170726_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='exam_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
