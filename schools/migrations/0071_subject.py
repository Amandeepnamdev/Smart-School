# Generated by Django 3.0.6 on 2020-07-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0070_onlineclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
