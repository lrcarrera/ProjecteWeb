# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-16 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.IntegerField(choices=[(1, 'Customer'), (2, 'Seller'), (3, 'Administrator')], default=1),
        ),
    ]