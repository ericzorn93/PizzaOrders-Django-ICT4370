"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('edit_order', include('pizzas.urls')),
    path('admin/', admin.site.urls),
    path('login', auth_views.login),
    path('', include('pizzas.urls')),
    path('menu', include('pizzas.urls')),
    path('about', include('pizzas.urls')),
    path('orders', include('pizzas.urls')),
    path('create', include('pizzas.urls')),
    path('closed_orders', include('pizzas.urls')),
    path('specific_order', include('pizzas.urls')),
    path('home', include('pizzas.urls')),
]
