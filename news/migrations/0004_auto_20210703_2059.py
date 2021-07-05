# Generated by Django 3.2.4 on 2021-07-03 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210703_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 59, 4, 171097, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.subrubric', verbose_name='Рубрика'),
        ),
    ]