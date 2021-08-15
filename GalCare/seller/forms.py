from django import forms
from django.db.models.base import Model
from django .forms import fields
from .models import Seller

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields="__all__"