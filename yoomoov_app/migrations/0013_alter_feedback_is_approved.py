# Generated by Django 3.2.20 on 2023-07-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoomoov_app', '0012_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='is_approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=25),
        ),
    ]