from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.core.mail import send_mail
from yoomoov_project.views import handler403, handler404, handler500
from .choices import (
    SIZE_CHOICES,
    LOCATION_CHOICES,
    COUNTY_CHOICES,
    STATUS_CHOICES,
    RATING_CHOICES,
    APPROVAL_CHOICES
)


class Van(models.Model):
    """
    Model for van listings.  SIZE, LOCATION AND COUNTY CHOICES
    are imported from choices.py, and managed through context_processors.py
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name="Unique Url Slug",
                            help_text="Example: your_van_name")
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
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default='0',
    )
    date_added = models.DateTimeField(default=timezone.now, blank=True)
    is_live = models.BooleanField(default=False)

    class Meta:
        """
        Meta class for ordering data set by latest date-added
        """
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Model for booking a van

    Fields added to notify user when booking status has changed
    """
    booking_number = models.CharField(max_length=200, unique=True, blank=True,
                                      editable=True)

    van = models.ForeignKey(Van, on_delete=models.DO_NOTHING)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100,
                             verbose_name="Enter customer's phone number",)

    van_name = models.CharField(max_length=250, default='Enter name of van')
    van_size = models.CharField(max_length=75, choices=SIZE_CHOICES,
                                default='Small')
    van_location = models.CharField(max_length=75, choices=LOCATION_CHOICES,
                                    default='Birmingham')
    van_county = models.CharField(max_length=75, choices=COUNTY_CHOICES,
                                  default='Cardiff')

    date_required = models.DateField()
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_updated = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES,
                              default='Pending')
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Total Price',
        default='0'
    )
    user_id = models.IntegerField(blank=True, default='0')

    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Fields for status change to notify user
    is_approved_notified = models.BooleanField(default=False)
    is_completed_notified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Super Save Method saves the data to the db, to create
        an id which is then used to create a unique booking
        number, which is then saved again to the database

        An Email notification is sent to the bookingform email
        and the admin_user email
        """
        super().save(*args, **kwargs)

        admin_user = User.objects.get(username='admin')

        if not self.booking_number:
            self.booking_number = str(self.id + 1000)
            super().save(update_fields=["booking_number"])

        if self.status == 'Approved' and not self.is_approved_notified:
            # Send email
            send_mail(
                'Booking ' + str(self.booking_number) + ' Approved',
                'Your booking ' + str(self.booking_number) + ' ' +
                self.van_name + ' has been approved. Please login to your '
                'Dashboard for more details. Kind regards, YooMoov Admin Team',
                'yoomoovyoo@gmail.com',
                [self.email, admin_user.email],
                fail_silently=False,
            )

            # Set is_approved_notified to True since the user has been
            # notified now
            self.is_approved_notified = True
            super().save(update_fields=["is_approved_notified"])

        # Check if the status has changed to 'Completed' and the user hasn't
        # been notified yet
        elif self.status == 'Completed' and not self.is_completed_notified:
            # Send email
            send_mail(
                'Booking ' + str(self.booking_number) + ' Completed',
                'Your booking ' + str(self.booking_number) + ' ' +
                self.van_name + ' has been completed. Please login to your '
                'Dashboard to leave feedback. Kind regards, YooMoov Admin '
                'Team',
                'yoomoovyoo@gmail.com',
                [self.email, admin_user.email],
                fail_silently=False,
            )

            # Set is_completed_notified to True since the user has been
            # notified now
            self.is_completed_notified = True
            super().save(update_fields=["is_completed_notified"])

    class Meta:
        """
        Meta class for ordering bookings data by next booking due date
        """
        ordering = ['-date_required']

    def __str__(self):
        return self.booking_number


class Feedback(models.Model):
    """
    Model for capturing feedback
    """
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)

    booking_number = models.CharField(max_length=200, unique=True,
                                      blank=True, editable=True)
    van_name = models.CharField(max_length=250, default='Enter name of van')

    title = models.CharField(max_length=200, unique=True)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    is_approved = models.CharField(max_length=25, choices=APPROVAL_CHOICES,
                                   default='Pending')
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    date_last_updated = models.DateTimeField(default=timezone.now, blank=True)

    # Field for status change to notify user
    is_approved_notified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Super save method to update the approval status of the feedback, which
        triggers an email notification to the user and the admin_user
        """
        admin_user = User.objects.get(username='admin')

        if self.is_approved == 'Approved' and not self.is_approved_notified:
            # Send email
            send_mail(
                'Feedback for ' + str(self.booking_number) + ' Approved',
                'Your feedback for booking ' + str(self.booking_number) + ' '
                + self.van_name + ' has been approved and published. Please '
                'login to your Dashboard to view. Kind regards, YooMoov Admin '
                'Team',
                'yoomoovyoo@gmail.com',
                [self.email, admin_user.email],
                fail_silently=False,
            )

            # Set is_approved_notified to True since the user has been
            # notified now
            self.is_approved_notified = True

        super().save(*args, **kwargs)

    class Meta:
        """
        Meta class for ordering feedback by latest date-created
        """
        ordering = ['-date_created']

    def __str__(self):
        return self.title
