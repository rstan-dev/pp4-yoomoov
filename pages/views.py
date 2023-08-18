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

