# Generated by Django 2.2.4 on 2020-06-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlmonitoring', '0010_auto_20200611_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmonitoring',
            name='password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='urlmonitoring',
            name='url',
            field=models.CharField(max_length=25),
        ),
    ]
