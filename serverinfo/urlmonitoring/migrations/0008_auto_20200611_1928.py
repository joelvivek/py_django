# Generated by Django 2.2.4 on 2020-06-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlmonitoring', '0007_auto_20200611_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlmonitoring',
            name='ownerphnosecond',
        ),
        migrations.AlterField(
            model_name='urlmonitoring',
            name='ownerphnofirst',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
