from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Products(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=150)
    product_brand = models.CharField(max_length=150)
    product_manufacturer = models.CharField(max_length=150)
    price = models.FloatField()
