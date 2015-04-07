# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='teams',
        ),
        migrations.AddField(
            model_name='match',
            name='away',
            field=models.ForeignKey(related_name='away', default=None, to='sports.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home',
            field=models.ForeignKey(related_name='home', default=None, to='sports.Team'),
        ),
    ]
