# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zabbix', '0003_subsystem_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsystem_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='subsystem_info',
            name='subsystemname',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
