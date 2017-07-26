# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classspec_id', models.BigIntegerField()),
                ('job_description_link', models.URLField()),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('qualifications', models.TextField()),
                ('career_ladder', models.URLField()),
                ('exam_notes', models.TextField()),
                ('salary_low', models.IntegerField()),
                ('salary_high', models.IntegerField()),
                ('exam_date', models.DateField()),
                ('categories', models.ManyToManyField(blank=True, to='jobs.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OccupationalCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='occupational_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.OccupationalCategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='related_keywords',
            field=models.ManyToManyField(blank=True, to='jobs.RelatedKeywords'),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(blank=True, to='jobs.Skills'),
        ),
    ]