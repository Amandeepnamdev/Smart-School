# Generated by Django 3.0.6 on 2020-07-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0082_auto_20200704_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='enroll_form_subject',
            field=models.CharField(default='', max_length=50),
        ),
    ]
