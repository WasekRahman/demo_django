# Generated by Django 2.1.3 on 2019-04-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190405_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdffile',
            field=models.FileField(upload_to='PDFs/'),
        ),
    ]
