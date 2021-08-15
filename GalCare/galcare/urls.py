from django.urls import path
from .views import sell_product


urlpatterns=[
    path("sell/", sell_product, name="sell_product"),
]