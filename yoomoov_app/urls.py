from . import views
from django.urls import path

urlpatterns = [
    path('', views.test_view, name='test'),
]