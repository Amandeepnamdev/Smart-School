# Generated by Django 3.0.8 on 2020-08-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0088_schoolreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img_link', models.URLField(max_length=300)),
                ('product_link', models.URLField(max_length=300)),
                ('product_name', models.CharField(default='', max_length=100)),
                ('product_detail', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
