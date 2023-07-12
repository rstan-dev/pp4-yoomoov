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
        ('BIRMINGHAM', 'Birmingham'),
        ('BRIGHTON', 'Brighton'),
        ('CARDIFF', 'Cardiff'),
        ('GLASGOW', 'Glasgow'),
        ('LEEDS', 'Leeds'),
        ('LIVERPOOL', 'Liverpool'),
        ('LONDON', 'London'),
        ('MANCHESTER', 'Manchester'),
        ('NEWCASTLE', 'Newcastle'),
        ('SHEFFIELD', 'Sheffield'),
        ('SOUTHAMPTON', 'Southampton'),

    )

    COUNTY_CHOICES = (
        ('CARDIFF', 'Cardiff'),
        ('EAST SUSSEX', 'East Sussex'),
        ('GLASGOW CITY', 'Glasgow City'),
        ('GREATER LONDON', 'Greater London'),
        ('GREATER MANCHESTER', 'Greater Manchester'),
        ('HAMPSHIRE', 'Hampshire'),
        ('MERSEYSIDE', 'Merseyside'),
        ('SOUTH YORKSHIRE', 'South Yorkshire'),
        ('TYNE AND_WARE', 'Tyne & Ware'),
        ('WEST MIDLANDS', 'West Midlands'),
        ('WEST YORKSHIRE', 'West Yorkshire'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Unique Url Slug", help_text="Example: your_van_name")
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

