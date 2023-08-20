from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact/<str:slug>', views.contact, name='contact_from_van'),
]
