# Generated by Django 3.2.20 on 2023-07-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoomoov_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='van',
            name='load_area_height',
            field=models.DecimalField(decimal_places=1, help_text='Specify the load area with one decimal place', max_digits=2, verbose_name='Load Area Height in metres'),
        ),
        migrations.AlterField(
            model_name='van',
            name='load_area_length',
            field=models.DecimalField(decimal_places=1, help_text='Specify the load area with one decimal place', max_digits=2, verbose_name='Load Area Length in metres'),
        ),
        migrations.AlterField(
            model_name='van',
            name='load_area_width',
            field=models.DecimalField(decimal_places=1, help_text='Specify the load area with one decimal place', max_digits=2, verbose_name='Load Area Width in metres'),
        ),
    ]