from django.db import models


# Create your models here.
class Employee_Detail(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=30)
    password = models.CharField(max_length=100)


class Next_of_kin_Detail(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ID_No = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=30)
    employee_name = models.CharField(max_length=100)
