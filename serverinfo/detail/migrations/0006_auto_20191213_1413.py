# Generated by Django 2.2.4 on 2019-12-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0005_auto_20191210_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverinfo',
            name='endpoint',
            field=models.CharField(default='True', max_length=255),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='url',
            field=models.CharField(default='True', max_length=8),
        ),
    ]
