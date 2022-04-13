# Generated by Django 3.0.8 on 2020-08-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0090_auto_20200809_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img_a_src',
            field=models.URLField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='product_img_src',
            field=models.URLField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img_link',
            field=models.URLField(default='', max_length=1000),
        ),
    ]
