# Generated by Django 3.0.6 on 2020-06-17 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0038_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.Teacher'),
        ),
    ]