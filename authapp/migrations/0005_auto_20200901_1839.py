# Generated by Django 2.2.4 on 2020-09-01 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20200901_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 15, 39, 46, 168470, tzinfo=utc)),
        ),
    ]
