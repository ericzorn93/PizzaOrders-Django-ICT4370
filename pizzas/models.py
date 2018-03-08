from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.utils import timezone


# Create your models here.
class Pizza(models.Model):
    """Creates the Pizza Model with Customer's Name"""
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Toppings(models.Model):
    """Inherits Name as a Foreign Key and Allows for Pizza Toppings"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza = models.CharField(max_length=100)
    name = models.CharField(max_length=50)


class FulfilledOrders(models.Model):
    """Creates Filled Orders for Pizzas"""
    order_fulfilled = models.BooleanField()
    date_time_fulfilled = models.DateTimeField(auto_now=timezone.now)
