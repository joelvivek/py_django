# Generated by Django 2.2.4 on 2020-06-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlmonitoring', '0006_auto_20200611_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmonitoring',
            name='ownerphnofirst',
            field=models.IntegerField(default=74830, max_length=5),
        ),
        migrations.AlterField(
            model_name='urlmonitoring',
            name='ownerphnosecond',
            field=models.IntegerField(default=36389, max_length=5),
        ),
    ]
