from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('all_vans/', views.all_vans, name='all_vans'),
    path('search', views.van_search, name='search'),

]