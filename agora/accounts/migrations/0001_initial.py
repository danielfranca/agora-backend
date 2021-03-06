# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-01 22:32
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="format expected: '+999999999'", regex='^\\+?1?\\d{9,15}$')])),
                ('business_name', models.CharField(max_length=100)),
                ('business_address', models.CharField(max_length=255)),
                ('register_number', models.CharField(max_length=8)),
                ('business_sector', models.CharField(choices=[('RE', 'Retail'), ('PS', 'Professional Services'), ('FD', 'Food & Drink'), ('EN', 'Entertainment')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
