# Generated by Django 3.1.11 on 2021-05-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0011_auto_20201013_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='keywords',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
