# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-27 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20160327_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shisha',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shisha',
            name='flavour',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.TextField(),
        ),
    ]