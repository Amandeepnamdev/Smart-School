# Generated by Django 3.0.6 on 2020-06-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0058_auto_20200620_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_id2',
            field=models.IntegerField(default=0),
        ),
    ]
