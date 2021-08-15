from django import forms
from django.db.models.base import Model
from django .forms import fields
from .models import Product


class ProductSellingForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"