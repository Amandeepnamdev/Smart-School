# Generated by Django 3.0.6 on 2020-06-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs_name', models.CharField(max_length=100)),
                ('subs_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
