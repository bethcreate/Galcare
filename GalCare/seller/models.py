from django.db import models

# Create your models here.
class Seller(models.Model):
    first_name=models.CharField(
        max_length=100
    )

    last_name=models.CharField(
        max_length=100, 
    )

    phone_number=models.CharField(
        max_length=15 
    )

    id_number=models.CharField(
        max_length=20
    )

 