# Generated by Django 2.2.4 on 2019-11-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='statuscode',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
