from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('all_vans/', views.all_vans, name='all_vans'),
    path('services/', views.services, name='services'),
]