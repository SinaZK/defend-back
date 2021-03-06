# Generated by Django 2.1.5 on 2020-02-06 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.ftp
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('author', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('price', models.IntegerField(default=0)),
                ('image', models.FileField(blank=True, null=True, upload_to=utils.ftp.UploadToPathAndRename('public_html/ebooks'))),
                ('dl_file', models.FileField(blank=True, null=True, upload_to=utils.ftp.UploadToPathAndRename('public_html/ebooks'))),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'EBook',
                'verbose_name_plural': 'EBooks',
            },
        ),
        migrations.CreateModel(
            name='EBookOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('checkout', 'Checkout'), ('paid', 'Paid')], default='checkout', max_length=30)),
                ('token', models.CharField(default=utils.utils.code_generator, max_length=30)),
                ('ebook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ebook.EBook')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
