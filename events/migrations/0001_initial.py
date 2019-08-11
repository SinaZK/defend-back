# Generated by Django 2.1.5 on 2019-08-11 11:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import utils.ftp


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='', max_length=300)),
                ('body', models.TextField(blank=True, default='')),
                ('location', models.TextField(blank=True, default='')),
                ('date', models.DateField(default=datetime.datetime(2019, 8, 11, 11, 25, 41, 868373, tzinfo=utc))),
                ('time', models.TimeField()),
                ('image', models.FileField(upload_to=utils.ftp.UploadToPathAndRename('public_html/events'))),
            ],
            options={
                'verbose_name': 'رویداد',
                'verbose_name_plural': 'رویداد\u200cها',
            },
        ),
    ]
