from django.db import models
from account.models import User
# Create your models here.


class Vehicle(models.Model):
    VEHICLE_TYPE = (
        ("TWO-WHEELER", "TWO-WHEELER"),
        ("THREE-WHEELER", "THREE-WHEELER"),
        ("FOUR-WHEELER","FOUR-WHEELER")
    )
    MANUFACTURE_COMPANY = (
        ("TATA", "TATA"),
        ("HYUNDAI", "HYUNDAI"),
        ("MG", "MG"),
        ("KIA", "KIA"),
        ("BMW", "BMW"),
        ("AUDI", "AUDI"),
        ("JAGUAR", "JAGUAR"),
        ("PORSCHE", "PORSCHE"),
        ("MERCEDES-BENZ", "MERCEDES-BENZ"),
        ("MINI COOPER", "MINI COOPER"),
        ("HERO ELECTRIC", "HERO ELECTRIC"),
        ("OLA ELECTRIC", "OLA ELECTRIC"),
        ("ATHER ENERGY", "ATHER ENERGY"),
        ("MAHINDRA ELECTRIC", "MAHINDRA ELECTRIC"),
        ("TVS", "TVS"),
        ("BAJAJ", "BAJAJ"),
        ("REVOLAT", "REVOLAT"),
        ("AMPERE EVS", "AMPERE EVS"),
        ("OKINAWA", "OKINAWA")

    )

    
    vehicle_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=30, choices=VEHICLE_TYPE, default='TWO-VEHCICLE')
    manufacture_company = models.CharField(max_length=100, choices=MANUFACTURE_COMPANY, default="TATA")
    model_name = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=14, unique=True)
    deleted = models.IntegerField(default=0, unique=False)

    def get_queryset(self):
        return Vehicle.objects.filter

    def __str__(self):
        return f"({self.vehicle_id},{self.model_name})"