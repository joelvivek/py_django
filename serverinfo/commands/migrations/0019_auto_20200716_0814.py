# Generated by Django 2.2.4 on 2020-07-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0018_auto_20200715_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountpoint',
            name='avail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mountpoint',
            name='filesystem',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mountpoint',
            name='size',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mountpoint',
            name='use',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mountpoint',
            name='used',
            field=models.CharField(max_length=255),
        ),
    ]