# Generated by Django 2.2.4 on 2020-07-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0020_applogfilesize_portinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
