from django.shortcuts import render

# Create your views here.
from .forms import SellerRegistrationForm
from django .shortcuts import render
from .models import Seller 

def register_seller(request):
    if request.method=="POST":
        form = SellerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=SellerRegistrationForm()
    return render(request,"register_seller.html",{"form":form, "Name":"Rissa"})

