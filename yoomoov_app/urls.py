from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('all_vans/', views.all_vans, name='all_vans'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('search', views.van_search, name='search'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_booking/', views.createBooking, name='create_booking'),
    path('update_booking/<str:booking_id', views.updateBooking, name='update_booking'),
    path('<slug:slug>/', views.van_detail, name='van_detail'),

]
