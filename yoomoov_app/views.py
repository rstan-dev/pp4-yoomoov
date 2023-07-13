from django.shortcuts import render
from django.views import generic, View
from .models import Van


def home(request):
    vans = Van.objects.all().filter(is_live=True).order_by('-date_added')

    context = {
        'vans': vans,
    }

    return render(request, 'index.html', context)

# class VanList(generic.ListView):
#     model = Van
#     queryset = Van.objects.filter(is_live=True).order_by('-date_added')
#     template_name = 'index.html'
#     paginate_by = 3
