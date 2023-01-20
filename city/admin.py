from django.contrib import admin

from city.models import City

# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
  
    list_display = ('city_id', 'city_name',  )
    search_fields = ('city_id', 'city_name', )
   