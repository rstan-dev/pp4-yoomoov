from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from cloudinary.models import CloudinaryField


class Van(models.Model):
    """
    Model for van listings
    """

    SIZE_CHOICES = (
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large')
    )

    LOCATION_CHOICES = (
        ('LONDON', 'London'),
        ('MANCHESTER', 'Manchester'),
        ('BIRMINGHAM', 'Birmingham'),
        ('LEEDS', 'Leeds'),
        ('GLASGOW', 'Glasgow'),
        ('SOUTHAMPTON', 'Southampton'),
        ('LIVERPOOL', 'Liverpool'),
        ('NEWCASTLE', 'Newcastle'),
        ('SHEFFIELD', 'Sheffield'),
        ('BRIGHTON', 'Brighton'),
        ('CARDIFF', 'Cardiff'),
    )

    COUNTY_CHOICES = (
        ('GREATER LONDON', 'Greater London'),
        ('GREATER MANCHESTER', 'Greater Manchester'),
        ('WEST MIDLANDS', 'West Midlands'),
        ('WEST YORKSHIRE', 'West Yorkshire'),
        ('GLASGOW CITY', 'Glasgow City'),
        ('HAMPSHIRE', 'Hampshire'),
        ('MERSEYSIDE', 'Merseyside'),
        ('TYNE AND_WARE', 'Tyne & Ware'),
        ('SOUTH YORKSHIRE', 'South Yorkshire'),
        ('EAST SUSSEX', 'East Sussex'),
        ('CARDIFF', 'Cardiff'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    size = models.CharField(max_length=75, choices=SIZE_CHOICES)
    location = models.CharField(max_length=75, choices=LOCATION_CHOICES)
    county = models.CharField(max_length=75, choices=COUNTY_CHOICES)
    crew = models.IntegerField(default=1)
    suitable_for = models.TextField(max_length=200)
    load_area_width = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        verbose_name='Load Area Width in metres',
        help_text='Specify the load area with one decimal place',
    )
    load_area_height = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        verbose_name='Load Area Height in metres',
        help_text="Specify the load area with one decimal place",
    )
    load_area_length = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        verbose_name='Load Area Length in metres',
        help_text="Specify the load area with one decimal place",
    )
    image = CloudinaryField('image', default='placeholder')
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    is_live = models.BooleanField(default=False)

    class Meta:
        """
        Meta class for ordering data set by latest date-added
        """
        ordering = ['-date_added']

    def __str__(self):
        return self.name

