from django .urls import path
from .views import register_seller


urlpatterns=[
    path("register", register_seller, name="register_seller"),
]