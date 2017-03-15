# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifs', '0006_auto_20160909_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
