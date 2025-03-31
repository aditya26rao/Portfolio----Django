"""
URL configuration for Porfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from App1.views import index, submit_form, success_view
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('aditya/',index,name='aditya'),
    path('submit/', submit_form, name='submit_form'),
    path('success/', success_view, name='success'),  # Route for success page
]

