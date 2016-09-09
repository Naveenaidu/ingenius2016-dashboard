# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifs', '0002_auto_20160907_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='expire_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='shown',
            field=models.BooleanField(default=True),
        ),
    ]
