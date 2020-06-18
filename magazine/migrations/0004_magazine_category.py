# Generated by Django 2.1.5 on 2020-06-18 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20200619_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='magazine.MagazineCategory', verbose_name='magazines'),
        ),
    ]
