from django.contrib import admin

from station.models import Station

# Register your models here.

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
  
    list_display = ('user_id', 'station_name', 'connectors', 'station_id','status',)
    search_fields = ()
    ordering = ( )
