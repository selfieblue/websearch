# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imagesmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('imageid', models.CharField(max_length=50)),
                ('linkid', models.CharField(max_length=50)),
                ('imageurl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='linkmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('linkid', models.CharField(max_length=50)),
                ('linkurl', models.CharField(max_length=200)),
            ],
        ),
    ]
