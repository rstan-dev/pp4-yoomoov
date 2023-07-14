from .models import Van


def location_choices(request):
    return {'location_choices': dict(Van.LOCATION_CHOICES)}


def van_size_choices(request):
    return {'van_size_choices': dict(Van.SIZE_CHOICES)}


def county_choices(request):
    return {'county_choices': dict(Van.COUNTY_CHOICES)}
