# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0003_remove_linkmodel_linktxt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagesmodel',
            name='imageid',
        ),
    ]
