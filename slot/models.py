from django.db import models
from account.models import User
from station.models import Station

# Create your models here.

class Slot(models.Model):
    CURRENT_STATUS_CHOICE = (
        ("AVAILABLE", "AVAILABLE"),
        ("OCCUPIED", "OCCUPIED")
    )
    slot_id = models.AutoField(primary_key=True)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot_name = models.CharField(max_length=30)
    per_unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    current_status = models.CharField(max_length=20, choices=CURRENT_STATUS_CHOICE, default="AVAILABLE")
    
    
    created_by = models.IntegerField(default=1)
    update_by = models.IntegerField(default=1)

    deleted = models.IntegerField(default=0, unique=False)

    

    def __str__(self):
        return f"{self.slot_name}"