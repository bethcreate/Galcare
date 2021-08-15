from django.db import models

# Create your models here.
class Product(models.Model):
    brand=models.CharField(
        max_length=100
    )

    quantity=models.PositiveSmallIntegerField(
        max_length=200, null=True
    )

    design=models.CharField(
        max_length=100, null=True
    )

    serial_number=models.CharField(
        max_length=50
    )

    image=models.ImageField(
        upload_to='uploads',blank=True, null=True
    )

    seller=models.CharField(
        max_length=100
    )







