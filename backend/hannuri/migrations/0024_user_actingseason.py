# Generated by Django 3.2.5 on 2022-01-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hannuri', '0023_auto_20210911_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='actingSeason',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
