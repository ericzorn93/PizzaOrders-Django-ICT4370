from django.conf.urls import url
from django.contrib import admin
from . import views
from . models import Pizza, Toppings
from django.contrib.auth.views import login
from django.views.generic import DetailView, ListView
# from . import views

urlpatterns = [
    url(r'edit_order/(?P<pk>\d+)/', views.edit_order),
    url(r'closed_orders/', views.closed_orders),
    url(r'home/', views.homepage),
    url(r'orders/', views.orders),
    url(r'specific_order/(?P<pk>\d+)/', views.specific_order),
    url(r'menu/', views.menu),
    url(r'about/', views.about),
    url(r'admin/', admin.site.urls),
    url(r'^$', login),
    url(r'create/', views.create),
    url(r'accounts/profile', views.Profile),
    url(r'order_info/', views.order_info),
]
