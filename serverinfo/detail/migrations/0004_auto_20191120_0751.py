# Generated by Django 2.2.4 on 2019-11-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_auto_20191120_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='statuscode',
            field=models.CharField(default='True', max_length=3),
        ),
    ]
