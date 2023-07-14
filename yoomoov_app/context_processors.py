from .models import Van


def location_choices(request):
    return {'location_choices': dict(Van.LOCATION_CHOICES)}
