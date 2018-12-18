"""OnlinerPropertySale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openadmin/',admin.site.urls),
    path('homepage/',views.Homepage),
    path('',TemplateView.as_view(template_name="index.html")),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('sales/',TemplateView.as_view(template_name="sales.html")),
    path('contact/',TemplateView.as_view(template_name="contact.html")),
    path('registration/',views.Registration),
    path('userdetails/',views.userdetails),
    path('login/',views.login),
    path('loginvalidate/',views.loginvalidate),
    path('register1/',views.userdetails),
    path('register/',views.registeruser),
    path('welcomeuser/',views.welcomeuser),
    path('viewprofile/',views.viewprofile),
    path('AddProperties/',views.AddProperties),
    path('add_property_user/',views.add_property_user),
    path('update/',views.update),
    path('perssion/',views.perssion),
]
