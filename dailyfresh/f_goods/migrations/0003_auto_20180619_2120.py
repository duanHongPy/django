# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f_goods', '0002_auto_20180619_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodinfo',
            name='gsales',
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
    ]
