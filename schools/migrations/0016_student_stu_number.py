# Generated by Django 3.0.6 on 2020-06-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0015_auto_20200610_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_number',
            field=models.IntegerField(default=0),
        ),
    ]
