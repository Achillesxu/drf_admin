# Generated by Django 2.2.13 on 2021-01-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_onlineusers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlogs',
            name='desc',
            field=models.CharField(max_length=128, verbose_name='描述'),
        ),
    ]
