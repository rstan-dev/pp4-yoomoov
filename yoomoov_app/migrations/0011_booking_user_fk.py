# Generated by Django 3.2.20 on 2023-07-25 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yoomoov_app', '0010_booking_van_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
