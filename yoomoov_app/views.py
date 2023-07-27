from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from .models import Van, Booking, Feedback
from django.contrib import messages
from .forms import BookingForm, FeedbackForm
import logging
from django.db.models import Exists, OuterRef
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def home(request):
    """
    Gets latest 3 van listings from database
    and renders on Home page
    """
    vans = Van.objects.all().filter(is_live=True).order_by('-date_added')[:3]

    context = {
        'vans': vans,
    }

    return render(request, 'index.html', context)


def all_vans(request):
    """
    Gets all van listings from database
    and renders on All Vans page
    """
    vans = Van.objects.all().filter(is_live=True).order_by('-date_added')

    context = {
        'vans': vans,
    }

    return render(request, 'all_vans.html', context)


def services(request):
    """
    Renders Services page
    """
    return render(request, 'services.html')


def contact(request, slug=None):
    """
    Renders Contact page form and submits user data via email to the administrator and
    to the user.

    Contact view is accessed directly via the Contact link in the menu bar, or via
    the van_detail page.

    If the contact form is accessed directly by the menu bar, the page redirects to the home page.
    if the contact form is accessed by the van_detail page, the email includes the van details and
    redirects the user back to the van_detail page
    """

    van = None
    if slug is not None:
        van = get_object_or_404(Van, slug=slug)

    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = 'Van Enquiry'
        if van is not None:
            subject += ' ' + van.name

        send_mail(
            subject,
            'There has been an enquiry from: ' + name + ' from email: ' + email + '. Their message is as follows: "' + message + '." An administrator will respond within 24 hours.',
            'yoomoov@outlook.com',
            [email, 'yoomoov@outlook.com', 'russ.smith1001@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Your message has been sent! We will respond within 24 hours.")

        if van is not None:
            return redirect('van_detail', slug=slug)
        else:
            return redirect('home')

    context = {
        'van': van
    }

    return render(request, 'contact.html', context)


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

    van_feedbacks = Feedback.objects.filter(is_approved='Approved', van=van).order_by('date_created')

    context = {
        'van': van,
        'vans': vans,
        'van_feedbacks': van_feedbacks
    }

    return render(request, 'van_detail.html', context)


def van_search(request):
    """
    Renders a list of vans using the Search choices from the Hero
    Van Finder Box.
    """

    queryset_vans = Van.objects.order_by('-date_added').filter(is_live=True)

    # Van Size Filter
    if 'van-size' in request.GET:
        van_size = request.GET['van-size']
        if van_size:
            queryset_vans = queryset_vans.filter(size__iexact=van_size)

    # Location Filter
    if 'location' in request.GET:
        location_selection = request.GET['location']
        if location_selection:
            queryset_vans = queryset_vans.filter(location__iexact=location_selection)

    # County Filter
    if 'county' in request.GET:
        county_selection = request.GET['county']
        if county_selection:
            queryset_vans = queryset_vans.filter(county__iexact=county_selection)

    values = {
        'size': None,
        'location': None,
        'county': None
        }

    context = {
        'values': values,
        'vans': queryset_vans
    }

    return render(request, 'van_filter.html', context)


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
    # bookings = Booking.objects.filter(user_id=request.user.id).order_by('date_required')

    vans = Van.objects.all()

    form = BookingForm()

    feedbacks = Feedback.objects.filter(user_fk=request.user).order_by('date_created')

    # Query to check whether each booking has associated feedback.
    has_feedback = Feedback.objects.filter(user_fk=request.user, booking_number=OuterRef('booking_number'))

    # Annotate each booking with a flag indicating whether it has feedback.
    bookings = Booking.objects.filter(user_id=request.user.id).order_by('date_required').annotate(has_feedback=Exists(has_feedback))



    context = {
        'bookings': bookings,
        'vans': vans,
        'form': form,
        'feedbacks': feedbacks,
    }
    return render(request, 'dashboard.html', context)


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

    bookings = Booking.objects.filter(user_id=request.user.id).order_by('date_required')

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
            booking.save()

            send_mail(
                'New booking for: ' + booking.van_name,
                'There has been a new booking created for ' + booking.van_name + ', for: ' + booking.date_required.strftime('%d %B %Y') + ' . Please login to your Dashboard to view the Status. Kind regards, YooMoov',
                'yoomoov@outlook.com',
                [booking.email, 'yoomoov@outlook.com', 'russ.smith1001@gmail.com'],
            fail_silently=False
            )

            messages.success(request, 'Your booking has been created successfully')
            return redirect('dashboard')

        form = BookingForm()

    context = {
        'bookings': bookings,
        'vans': vans,
        'form': form,
        }

    return render(request, 'dashboard.html', context)


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
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        print('Printing POST', request.POST)
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
                'Updated booking for: ' + str(booking.booking_number) + ' ' + booking.van_name,
                'There has been a change to booking ' + str(booking.booking_number) + ' ' + booking.van_name + ', for: ' + booking.date_required.strftime('%d %B %Y') + ' . Please login to your Dashboard to view the Status. Kind regards, YooMoov',
                'yoomoov@outlook.com',
                [booking.email, 'yoomoov@outlook.com', 'russ.smith1001@gmail.com'],
            fail_silently=False
            )

            messages.success(request, 'Your booking has been updated successfully')
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'edit_booking.html', context)


def deleteBooking(request, pk):
    """
    Method to delete a specific booking.
    Booking objects are called using the booking id primary key (pk).
    User is taken to a dedicated delete_booking page with a confirmation
    message and a cancel button.
    User is redirected back to the dashboard on completion with a success
    messgae displayed on screen.
    """
    booking = Booking.objects.get(id=pk)
    if request.method == "POST":
        booking.delete()
        messages.success(request, 'Your booking has been successfully deleted')
        return redirect('dashboard')

    context = {
        'booking': booking
    }

    return render(request, 'delete_booking.html', context)


def leaveFeedback(request, pk):

    booking = Booking.objects.get(id=pk)
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            print('Printing POST', request.POST)
            print("form is valid")
            feedback = form.save(commit=False)
            feedback.booking = booking
            feedback.van = booking.van
            feedback.booking_number = booking.booking_number
            feedback.van_name = booking.van_name
            feedback.user_fk = request.user
            feedback.save()
            print("feedback saved successfully")
            messages.success(request, 'Your feedback has been submitted for review successfully')
            return redirect('dashboard')
        else:
            print("Form is not valid:", form.errors)

    context = {
        'form': form,
        'booking': booking,
    }

    return render(request, 'leave_feedback.html', context)

