from django.contrib import admin
from .models import Pizza, Toppings, FulfilledOrders

# Register your models here.


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Toppings)
class ToppingsAdmin(admin.ModelAdmin):
    pass


@admin.register(FulfilledOrders)
class FulfilledOrdersAdmin(admin.ModelAdmin):
    pass
