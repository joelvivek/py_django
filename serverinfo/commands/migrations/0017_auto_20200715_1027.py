# Generated by Django 2.2.4 on 2020-07-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0016_mountpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedata',
            name='hostname',
            field=models.CharField(max_length=32),
        ),
    ]
