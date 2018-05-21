# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0004_auto_20180518_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.IntegerField(choices=[(1, 'Customer'), (2, 'Seller')], default=1),
        ),
    ]
