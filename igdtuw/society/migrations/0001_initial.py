# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='soclist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]