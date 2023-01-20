from django.contrib import admin

from vehicle.models import Vehicle
# # Register your models here.

@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    list_display = ('vehicle_type', 'manufacture_company', 'user_id')
