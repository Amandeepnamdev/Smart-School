# Generated by Django 3.0.6 on 2020-06-09 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_auto_20200609_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstudent',
            name='std_date',
        ),
    ]
