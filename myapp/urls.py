"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pdf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer_service_resume/', views.customer_service_resume, name="customer_service_resume"),
    path('construction_resume/', views.construction_resume, name="construction_resume"),
    path('security_resume/', views.security_resume, name="security_resume"),
    path('', views.about, name="about"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
    path('cookies_policy/', views.cookies_policy, name="cookies_policy"),
    path('customer_service_form/', views.customer_service_form, name='customer_service_form'),
    path('construction_form/', views.construction_form, name='construction_form'),
    path('security_form/', views.security_form, name='security_form'),
]
