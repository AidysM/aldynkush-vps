# Generated by Django 3.2.4 on 2021-07-05 19:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_new_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 19, 29, 9, 476977, tzinfo=utc)),
        ),
    ]