from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from .models import Van, Booking, Feedback
from django.contrib import messages
from .forms import BookingForm, FeedbackForm, ContactForm
import logging
from django.db.models import Exists, OuterRef, Count
from django.core.mail import send_mail
from django.core.paginator import Paginator
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from yoomoov_project.views import handler403, handler404, handler500


@login_required
def dashboard(request):
    """
    Renders Bookings data, based on the logged in user id
    on the users dashboard.

    Calls the van object in order to render the van name list in the
    booking form dropdown

    Calls the BookingForm from forms.py to display when Create Booking button
    is clicked

    Calls the Feedback objects to display any feedback left by a user
    """

    vans = Van.objects.all()

    form = BookingForm()

    # Calls the order_by parameter - orders by date_updated as default
    order_by = request.GET.get('order_by', '-date_updated')

    feedbacks = Feedback.objects.filter(
        user_fk=request.user).order_by('date_created')

    # Query to check whether each booking has associated feedback -
    # adjusts "Leave Feedback" button to "Feedback Submitted"
    has_feedback = Booking.objects.filter(user_fk=request.user,
                                          booking_number=OuterRef(
                                            'booking_number'))

    # Annotate each booking with a flag indicating whether it has feedback.
    bookings = Booking.objects.filter(
        user_fk=request.user.id).order_by(order_by).annotate(
        has_feedback=Exists(Feedback.objects.filter(booking=OuterRef('pk')))
    )

    # Paginator for bookings table
    bookings_paginator = Paginator(bookings, 4)
    bookings_page_number = request.GET.get('bookings_section')
    page_bookings = bookings_paginator.get_page(bookings_page_number)

    # Paginator for feedback table
    feedback_paginator = Paginator(feedbacks, 3)
    feedback_page_number = request.GET.get('feedback_section')
    page_feedback = feedback_paginator.get_page(feedback_page_number)

    context = {
        'order_by': order_by,
        'bookings': page_bookings,
        'vans': vans,
        'form': form,
        'feedbacks': page_feedback,
        'has_feedback': has_feedback
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def createBooking(request):
    """
    Method for creating a booking and updating the Booking model.
    Displays the bookings by user on the dashboard.
    Calls the Van objects to display the van names in the booking form
    For any POST methods, the form is validated and booking fields are
    saved to the database.
    A success message is displayed on screen to the user.
    A new instance of the Booking Form is created to clear out the fields.
    """

    bookings = Booking.objects.filter(
        user_id=request.user.id).order_by('date_required')

    vans = Van.objects.all()

    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.van_name = booking.van.name
            booking.van_size = booking.van.size
            booking.van_location = booking.van.location
            booking.van_county = booking.van.county
            booking.price = booking.van.price
            booking.user_id = request.user.id
            booking.user_fk = request.user
            booking.save()

            send_mail(
                'New booking for: ' + booking.van_name,
                'There has been a new booking created for ' + booking.van_name
                + ', for: ' + booking.date_required.strftime('%d %B %Y') +
                ' . Please login to your Dashboard to view the Status. Kind '
                'regards, YooMoov',
                'yoomoovyoo@gmail.com',
                [booking.email, 'yoomoovyoo@gmail.com',
                                'russ.smith1001@gmail.com'],
                fail_silently=False
            )

            messages.success(request, 'Your booking has been created '
                                      'successfully')
            return redirect('dashboard')

        else:
            messages.error(request, form.non_field_errors())

    form = BookingForm()

    context = {
        'bookings': bookings,
        'vans': vans,
        'form': form,
        }

    return render(request, 'dashboard/dashboard.html', context)


@login_required
def editBooking(request, pk):
    """
    Method to edit/update booking details.
    Booking objects are called using the booking id primary key (pk).
    The booking form is generated, prefilled, on a dedicated edit_booking page
    with an instance of the booking.
    Any changes to the form are saved and a success message is displayed
    to the user.
    User is redirected back to the dashboard on completion.
    """
    booking = get_object_or_404(Booking, id=pk)
    form = BookingForm(instance=booking, initial={'booking_id': booking.id})

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.van_name = booking.van.name
            booking.van_size = booking.van.size
            booking.van_location = booking.van.location
            booking.van_county = booking.van.county
            booking.price = booking.van.price
            booking.status = 'Pending'
            booking.user_id = request.user.id
            booking.save()

            send_mail(
                'Updated booking for: ' + str(booking.booking_number) + ' '
                + booking.van_name, 'There has been a change to booking '
                + str(booking.booking_number) + ' ' + booking.van_name +
                ', for: ' + booking.date_required.strftime('%d %B %Y') +
                ' . Please login to your Dashboard to view the Status. Kind '
                'regards, YooMoov',
                'yoomoov@outlook.com',
                [booking.email, 'yoomoov@outlook.com',
                                'russ.smith1001@gmail.com'],
                fail_silently=False
            )

            messages.success(request, 'Your booking has been updated '
                                      'successfully')
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/edit_booking.html', context)


@login_required
def deleteBooking(request, pk):
    """
    Method to delete a specific booking.
    Booking objects are called using the booking id primary key (pk).
    User is taken to a dedicated delete_booking page with a confirmation
    message and a cancel button.
    User is redirected back to the dashboard on completion with a success
    messgae displayed on screen.
    """
    booking = get_object_or_404(Booking, id=pk)
    if request.method == "POST":
        booking.delete()

        send_mail(
                'Deleted booking for: ' + str(booking.booking_number) + ' '
                + booking.van_name, 'This booking has been deleted: '
                + str(booking.booking_number) + ' ' + booking.van_name +
                ', for: ' + booking.date_required.strftime('%d %B %Y') +
                '. Kind regards, YooMoov',
                'yoomoov@outlook.com',
                [booking.email, 'yoomoov@outlook.com',
                                'russ.smith1001@gmail.com'],
                fail_silently=False
            )

        messages.success(request, 'Your booking has been successfully deleted')
        return redirect('dashboard')

    context = {
        'booking': booking
    }

    return render(request, 'dashboard/delete_booking.html', context)


@login_required
def leaveFeedback(request, pk):

    booking = get_object_or_404(Booking, id=pk)
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.booking = booking
            feedback.van = booking.van
            feedback.booking_number = booking.booking_number
            feedback.van_name = booking.van_name
            feedback.user_fk = request.user
            feedback.save()

            send_mail(
                'Feedback left for: ' + str(booking.booking_number) + ' '
                + booking.van_name, 'A user has left feedback for: '
                + str(booking.booking_number) + ' ' + booking.van_name +
                ', for: ' + booking.date_required.strftime('%d %B %Y') +
                '. Please login to your dashboard for more details. Kind '
                'regards, YooMoov',
                'yoomoov@outlook.com',
                [booking.email, 'yoomoov@outlook.com',
                                'russ.smith1001@gmail.com'],
                fail_silently=False
            )

            messages.success(request, 'Your feedback has been submitted for '
                                      'review successfully')
            return redirect('dashboard')
        else:
            print("Form is not valid:", form.errors)

    context = {
        'form': form,
        'booking': booking,
    }

    return render(request, 'dashboard/leave_feedback.html', context)


def van_detail(request, slug):
    """
    Renders Van Detail page, by requesting all vans
    that are live, with a given unique slug

    Calls the Van.object to link the Booking Modal
    van select dropdown

    Calls Feedback.object to call any feedback specific to a van
    to display on van detail page
    """

    queryset = Van.objects.filter(is_live=True)

    van = get_object_or_404(queryset, slug=slug)

    vans = Van.objects.all()

    van_feedbacks = Feedback.objects.filter(is_approved='Approved',
                                            van=van).order_by('date_created')

    context = {
        'van': van,
        'vans': vans,
        'van_feedbacks': van_feedbacks
    }

    return render(request, 'dashboard/van_detail.html', context)


class CustomLoginView(LoginView):
    """
    Custom Login View to activate validation messages
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
