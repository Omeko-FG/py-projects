from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Car(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE)

    plate_number=models.CharField(max_length=12)
    brand=models.CharField(max_length=32)
    model=models.CharField(max_length=32)
    year=models.PositiveIntegerField()
    gear=models.PositiveSmallIntegerField()
    rent_per_day=models.PositiveBigIntegerField()
    availability=models.BooleanField()

    def __str__(self):
        return f"{self.plate_number}"

class Reservation(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE)

    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    # customer= models.ForeignKey(User, on_delete=models.CASCADE)

    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.start_date} && {self.end_date}"
    

