# Generated by Django 2.2.4 on 2020-05-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0006_remove_executecommand_command'),
    ]

    operations = [
        migrations.CreateModel(
            name='onboardserver',
            fields=[
                ('ip', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('project', models.CharField(default='True', max_length=15)),
                ('env', models.CharField(default='True', max_length=7)),
            ],
        ),
    ]
