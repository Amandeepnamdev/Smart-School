# Generated by Django 3.0.6 on 2020-06-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0064_auto_20200624_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(default='', max_length=500)),
                ('notification_link', models.CharField(default='', max_length=100)),
            ],
        ),
    ]