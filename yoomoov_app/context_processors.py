from .choices import SIZE_CHOICES, LOCATION_CHOICES, COUNTY_CHOICES, STATUS_CHOICES


def location_choices(request):
    return {'location_choices': LOCATION_CHOICES}


def van_size_choices(request):
    return {'van_size_choices': SIZE_CHOICES}


def county_choices(request):
    return {'county_choices': COUNTY_CHOICES}
