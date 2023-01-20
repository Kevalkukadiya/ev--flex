from django.db import models
from account.models import User
from state.models import State
from city.models import City
from area.models import Area


# Create your models here.
class Station(models.Model):    
    STAUTUS_CHOICE = (
        ("ACTIVE", "ACTIVE"),
        ("INACTIVE", "INACTIVE")
        )
    DAY_CHOICE = (
        ("MONDAY", "MONDAY"),
        ("Tuesday", "TUESDAY"),
        ("WEDNESDAY", "WEDNESDAY"),
        ("THURSDAY", "THURSDAY"),
        ("FRIDAY", "FRIDAY"),
        ("SATURDAY", "SATURDAY"),
        ("SUNDAY", "SUNDAY"),
        ("ALL DAY", "ALL DAY")
    )

    station_id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station_name = models.CharField(unique= True,max_length=50)
    station_address = models.CharField(unique=True, max_length=255)
    connectors = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STAUTUS_CHOICE, default="ACTIVE")
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    open_day = models.CharField(max_length=20, choices=DAY_CHOICE, default="ALL DAY")
    # give_feedback = models.CharField(max_length=255, null=True)

    created_by = models.IntegerField(default=1)
    update_by = models.IntegerField(default=1)

    deleted = models.IntegerField(default=0, unique=False)

    def __str__(self):
        return f'{self.station_name}'