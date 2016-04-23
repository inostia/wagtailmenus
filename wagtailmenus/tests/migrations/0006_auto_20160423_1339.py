# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_auto_20160419_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='repeat_in_subnav',
            field=models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-menu for this page.", verbose_name='repeat in sub-menu'),
        ),
        migrations.AlterField(
            model_name='toplevelpage',
            name='repeat_in_subnav',
            field=models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-menu for this page.", verbose_name='repeat in sub-menu'),
        ),
    ]