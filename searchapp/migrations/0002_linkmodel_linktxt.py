# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkmodel',
            name='linktxt',
            field=models.CharField(default=datetime.datetime(2015, 11, 5, 14, 54, 4, 1326, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
