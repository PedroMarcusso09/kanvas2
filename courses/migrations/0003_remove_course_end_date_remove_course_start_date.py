# Generated by Django 4.2.6 on 2023-10-28 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
    ]
