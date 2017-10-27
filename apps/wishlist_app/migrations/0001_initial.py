# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('all_users', models.ManyToManyField(related_name='all_items', to='login_app.User')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_item', to='login_app.User')),
            ],
        ),
    ]
