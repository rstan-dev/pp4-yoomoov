from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Van


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
    """
    queryset = Van.objects.filter(is_live=True)
    van = get_object_or_404(queryset, slug=slug)

    return render(request, 'van_detail.html', {
        'van': van,
    })


def van_search(request):
    """
    Renders Van Search Results page with inputs from the Hero Search Box

    Uses conteXt_processor for Van.LOCATION_CHOICES, Van.SIZE_CHOICES and
    Van.COUNTY_CHOICES.
    """
    values = {
        'size': None,
        'location': None,
        'county': None
        }

    context = {
        'values': values,
    }

    return render(request, 'partials/_hero-search.html', context)
