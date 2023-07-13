from django.shortcuts import render
from .models import Van


def home(request):
    return render(request, 'index.html')

class VanList(generic.ListView):
    model = Van
    queryset = Van.objects.filter(is_live=True).order_by('-date_added')
    template_name = 'index.html'
    paginate_by = 3
