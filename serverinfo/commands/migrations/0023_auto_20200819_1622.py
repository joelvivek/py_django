# Generated by Django 2.2.4 on 2020-08-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0022_document_filelocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='errorresponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='null', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='executecommand',
        ),
    ]
