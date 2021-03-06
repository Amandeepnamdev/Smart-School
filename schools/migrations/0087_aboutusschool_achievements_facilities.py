# Generated by Django 3.0.8 on 2020-07-16 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0086_auto_20200714_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schools.Schools')),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schools.Schools')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schools.Schools')),
            ],
        ),
    ]
