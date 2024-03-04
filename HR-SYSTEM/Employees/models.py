from django.db import models


# Create your models here.


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    emp_code = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=30)
    position = models.CharField(max_length=60)

    def objects(self):
        return self

    def __str__(self):
        return self.fullname
