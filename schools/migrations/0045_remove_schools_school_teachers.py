# Generated by Django 3.0.6 on 2020-06-18 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0044_auto_20200618_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schools',
            name='school_teachers',
        ),
    ]
