# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('ques', models.CharField(max_length=200)),
                ('ans', models.TextField(max_length=500)),
                ('soc_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society.soclist')),
            ],
        ),
    ]
