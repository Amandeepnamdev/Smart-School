# Generated by Django 3.0.6 on 2020-06-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0033_teacher_teacher_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_gender',
            field=models.CharField(default='', max_length=50),
        ),
    ]