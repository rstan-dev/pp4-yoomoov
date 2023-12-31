# Generated by Django 3.2.20 on 2023-07-25 11:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yoomoov_app', '0011_booking_user_fk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(blank=True, max_length=200, unique=True)),
                ('van_name', models.CharField(default='Enter name of van', max_length=250)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('comment', models.TextField(max_length=500)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('is_approved', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('date_last_updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoomoov_app.booking')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('van', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoomoov_app.van')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
