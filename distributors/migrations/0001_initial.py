# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-21 13:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(default='root', max_length=30)),
                ('email', models.EmailField(default='email@email.com', max_length=255, unique=True, verbose_name='email address')),
                ('is_admin', models.BooleanField(default=False)),
                ('phoneNumber', models.IntegerField(max_length=12, null=True)),
                ('street', models.CharField(max_length=30, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('city', models.CharField(max_length=30, null=True)),
                ('postCode', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Customer'), (2, 'Seller')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('kms', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('color', models.CharField(default='Color', max_length=30)),
                ('registrationYear', models.PositiveIntegerField(default=0)),
                ('body', models.CharField(max_length=30, null=True)),
                ('fuelType', models.IntegerField(choices=[(1, 'Gasoline'), (2, 'Diesel'), (3, 'Electric'), (4, 'Hybrid')], default=1)),
                ('modelYear', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018)),
                ('maxTopSpeed', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500)])),
                ('doors', models.IntegerField(choices=[(1, '3 Doors'), (2, '5 Doors')], default=2)),
                ('seats', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=5)),
                ('availability', models.IntegerField(choices=[(1, 'Available'), (2, 'Sold')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inaugurationYear', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018)),
                ('shopName', models.CharField(max_length=30, null=True)),
                ('addr', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=120, null=True)),
                ('stateOrProvince', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModelReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('car', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='distributors.Car')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='carShop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='distributors.CarShop'),
        ),
    ]
