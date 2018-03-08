from django.forms import ModelForm
from .models import Pizza, Toppings, FulfilledOrders
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class FullNameForm(ModelForm):
    """Inherits from ModelForm and Pizza Model with User's Name"""
    class Meta:
        model = Pizza
        fields = ['name']


class ToppingForm(ModelForm):
    """Inherits from ModelForm and Topping Model with User's Pizza Topping and Name"""
    class Meta:
        model = Toppings
        fields = ['pizza', 'name']


# Create User Signup Form
class UserForm(forms.ModelForm):
    """Creates Default User Registration Form"""
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# New User Register Forms
class RegistrationForm(UserCreationForm):
    """Updated Version of User Registration Form"""
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # contact_email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=12)
    street_address = forms.CharField(required=True, max_length=100)
    second_street_address = forms.CharField(required=False, max_length=100, label="Second Street Address (Optional)")
    town = forms.CharField(required=True, max_length=100)
    zip_code = forms.CharField(required=True, max_length=5)
    state = forms.CharField(required=True, max_length=2)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'street_address',
            'second_street_address',
            'town',
            'zip_code',
            'state',
            'username',
        )


# class FulfilledOrderForm(ModelForm):
    # """Fulfilled Orders Model Form"""
    # class Meta:
    #     model = FulfilledOrders
    #     fields = ['order_fulfilled', 'date_time_fulfilled']


class EditOrderForm(ModelForm):
    """Edit Existing Order"""
    class Meta:
        model = Toppings
        fields = ['name', 'pizza']
