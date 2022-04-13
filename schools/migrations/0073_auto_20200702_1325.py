# Generated by Django 3.0.6 on 2020-07-02 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0072_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={},
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.Teacher'),
        ),
    ]
