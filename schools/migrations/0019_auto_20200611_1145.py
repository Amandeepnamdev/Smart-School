# Generated by Django 3.0.6 on 2020-06-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0018_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.AddField(
            model_name='student',
            name='fee_status',
            field=models.CharField(choices=[('OK', 'Submitted'), ('NO', 'Not_submitted')], default='', max_length=20),
        ),
    ]