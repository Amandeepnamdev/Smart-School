# Generated by Django 3.0.6 on 2020-06-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0045_remove_schools_school_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='schools',
            name='school_teachers',
            field=models.ManyToManyField(limit_choices_to={'teacher_school_id': 1}, to='schools.Teacher'),
        ),
    ]
