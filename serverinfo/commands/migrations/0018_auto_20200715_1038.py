# Generated by Django 2.2.4 on 2020-07-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0017_auto_20200715_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedata',
            name='usedspace',
            field=models.CharField(default='True', max_length=5),
        ),
    ]