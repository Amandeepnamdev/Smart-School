# Generated by Django 3.0.6 on 2020-06-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0036_auto_20200612_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='std_photo',
            field=models.ImageField(default='', upload_to='schools/images/'),
        ),
    ]
