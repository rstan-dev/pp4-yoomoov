# Generated by Django 3.2.20 on 2023-07-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoomoov_app', '0003_auto_20230712_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='van',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=6),
        ),
    ]
