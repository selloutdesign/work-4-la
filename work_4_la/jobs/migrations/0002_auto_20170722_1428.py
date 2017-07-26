# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='responsibilities',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='career_ladder',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='exam_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='qualifications',
            field=models.TextField(blank=True),
        ),
    ]
