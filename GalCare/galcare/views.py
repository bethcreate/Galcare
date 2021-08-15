from django.shortcuts import render
from .forms import ProductSellingForm
from django .shortcuts import render
from .models import Product

def sell_product(request):
    if request.method=="POST":
        form = ProductSellingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=ProductSellingForm()
    return render(request,"sell_product.html",{"form":form, "Name":"Samsung"})
