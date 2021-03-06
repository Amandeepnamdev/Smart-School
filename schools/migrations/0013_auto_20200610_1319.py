# Generated by Django 3.0.6 on 2020-06-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0012_auto_20200609_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='std_10_per',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_11_per',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_8_per',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_8_school',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_9_per',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_address2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_medium',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='std_zip',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='newstudent',
            name='std_class',
            field=models.IntegerField(default=0),
        ),
    ]
