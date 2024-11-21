# Generated by Django 4.2.6 on 2023-10-28 11:55

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_end_date_remove_course_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 28, 11, 55, 4, 349795, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
