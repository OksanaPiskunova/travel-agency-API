# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='comments',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.URLField(verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_tour', to='travel_agency_api.Tour', verbose_name='Tour'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_tour', to='travel_agency_api.Tour', verbose_name='Tour'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]