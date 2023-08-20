from . import views
from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_booking/', views.createBooking, name='create_booking'),
    path('edit_booking/<str:pk>', views.editBooking, name='edit_booking'),
    path('delete_booking/<str:pk>', views.deleteBooking,
         name='delete_booking'),
    path('leave_feedback/<str:pk>', views.leaveFeedback,
         name='leave_feedback'),
    path('<slug:slug>/', views.van_detail, name='van_detail'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
]
