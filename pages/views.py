from django.shortcuts import render
from yoomoov_app.models import Van


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
