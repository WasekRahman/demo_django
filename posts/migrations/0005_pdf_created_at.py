# Generated by Django 2.1.3 on 2019-04-14 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190405_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
