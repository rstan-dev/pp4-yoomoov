"""yoomoov_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from yoomoov_project import views

urlpatterns = [
    path('', include('contact.urls'), name="contact_urls"),
    path('admin/', admin.site.urls),
    path('', include('pages.urls'), name="pages_urls"),
    path('', include('yoomoov_app.urls'), name="yoomoov_urls"),
    path('accounts/', include('allauth.urls')),
]

# Custom error handlers
handler403 = 'yoomoov_project.views.handler403'
handler404 = 'yoomoov_project.views.handler404'
handler500 = 'yoomoov_project.views.handler500'
