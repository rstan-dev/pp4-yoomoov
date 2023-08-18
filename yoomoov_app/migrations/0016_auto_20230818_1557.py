# Generated by Django 3.2.20 on 2023-08-18 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yoomoov_app', '0015_feedback_is_approved_notified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date_last_updated',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='van',
            name='date_added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]