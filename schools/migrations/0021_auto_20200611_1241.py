# Generated by Django 3.0.6 on 2020-06-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0020_auto_20200611_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='status',
            new_name='fee_status',
        ),
    ]