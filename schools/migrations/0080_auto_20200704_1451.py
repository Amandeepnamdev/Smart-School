# Generated by Django 3.0.6 on 2020-07-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0079_enroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enroll_school_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.Schools'),
        ),
    ]
