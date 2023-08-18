from django.shortcuts import render
from yoomoov_app.models import Van
from django.core.paginator import Paginator


def home(request):
    """
    Gets latest 3 van listings from database
    and renders on Home page
    """
    vans = Van.objects.all().filter(is_live=True).order_by('-date_added')[:3]

    context = {
        'vans': vans,
    }

    return render(request, 'pages/index.html', context)


def services(request):
    """
    Renders Services page
    """
    return render(request, 'pages/services.html')


def all_vans(request):
    """
    Gets all van listings from database
    and renders on All Vans page, listed by most recent date added,
    using paginator to display 6 vans per page
    """
    vans = Van.objects.all().filter(is_live=True).order_by('-date_added')

    paginator = Paginator(vans, 6)
    page_number = request.GET.get('page')
    page_listings = paginator.get_page(page_number)

    context = {
        'vans': page_listings,
    }

    return render(request, 'pages/all_vans.html', context)


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
            queryset_vans = queryset_vans.filter(
                location__iexact=location_selection)

    # County Filter
    if 'county' in request.GET:
        county_selection = request.GET['county']
        if county_selection:
            queryset_vans = queryset_vans.filter(
                county__iexact=county_selection)

    values = {
        'size': None,
        'location': None,
        'county': None
        }

    context = {
        'values': values,
        'vans': queryset_vans
    }

    return render(request, 'pages/van_filter.html', context)