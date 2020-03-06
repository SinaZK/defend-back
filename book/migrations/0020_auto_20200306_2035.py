# Generated by Django 2.1.5 on 2020-03-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_bookorder_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_year',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]