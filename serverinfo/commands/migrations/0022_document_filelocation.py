# Generated by Django 2.2.4 on 2020-07-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0021_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filelocation',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
