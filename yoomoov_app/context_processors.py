from .choices import SIZE_CHOICES, LOCATION_CHOICES, COUNTY_CHOICES


def location_choices(request):
    return {'location_choices': dict(LOCATION_CHOICES)}


def van_size_choices(request):
    return {'van_size_choices': dict(SIZE_CHOICES)}


def county_choices(request):
    return {'county_choices': dict(COUNTY_CHOICES)}
