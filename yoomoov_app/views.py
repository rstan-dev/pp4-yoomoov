from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from .models import Van, Booking
from django.contrib import messages
from .forms import BookingForm



def home(request):
    """
    GETs latest 3 van listings from database
    and renders on Home page
    """
    vans = Van.objects.all().filter(is_live=True).order_by('-date_added')[:3]

    context = {
        'vans': vans,
    }

    return render(request, 'index.html', context)


def all_vans(request):
    """
    GETs all van listings frokm database
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


def contact(request):
    """
    Renders Contact page
    """
    return render(request, 'contact.html')


def van_detail(request, slug):
    """
    Renders Van Detail page, by requesting all vans
    that are live, with a given unique slug

    Calls the Van.object to link the Booking Modal
    van select dropdown
    """
    queryset = Van.objects.filter(is_live=True)
    van = get_object_or_404(queryset, slug=slug)

    vans = Van.objects.all()

    context = {
        'van': van,
        'vans': vans
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
    """
    bookings = Booking.objects.filter(user_id=request.user.id).order_by('date_required')

    # booking = get_object_or_404(Booking, id=booking_id)

    vans = Van.objects.all()

    form = BookingForm()

    context = {
        'bookings': bookings,
        'vans': vans,
        'form': form,
        # 'booking': booking
    }
    return render(request, 'dashboard.html', context)


def createBooking(request):

    bookings = Booking.objects.filter(user_id=request.user.id).order_by('date_required')

    # booking = get_object_or_404(Booking, id=booking_id)

    vans = Van.objects.all()

    form = BookingForm()

    if request.method == 'POST':
        print('Printing POST', request.POST)
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
            messages.success(request, 'Your booking has been created successfully')
            return redirect('dashboard')

        form = BookingForm()

    context = {
        'bookings': bookings,
        'vans': vans,
        'form': form,
        # 'booking': booking
        }

    return render(request, 'dashboard.html', context)


def editBooking(request, pk):

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
            booking.user_id = request.user.id
            booking.save()
            messages.success(request, 'Your booking has been updated successfully')
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'edit_booking.html', context)

