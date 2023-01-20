from django.contrib import admin

from area.models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
  
    list_display = ('area_id', 'area_name', )
    search_fields = ('area_id', 'area_name', )
   