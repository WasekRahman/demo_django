# Generated by Django 2.1.3 on 2019-04-14 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_pdf_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
