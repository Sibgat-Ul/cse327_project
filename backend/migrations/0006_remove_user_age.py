# Generated by Django 4.1 on 2024-05-22 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_course_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
