# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albumler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanatci', models.CharField(max_length=250)),
                ('album_adi', models.CharField(max_length=250)),
                ('album_turu', models.CharField(max_length=100)),
                ('album_kapagi', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Sarkilar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarki_adi', models.CharField(max_length=250)),
                ('dosya_turu', models.CharField(max_length=10)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzik.Albumler')),
            ],
        ),
    ]
