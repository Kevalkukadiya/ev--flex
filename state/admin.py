from django.contrib import admin
from state.models import State
# Register your models here.


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
  
    list_display = ('state_id', 'state_name', )
    search_fields = ('state_id', 'state_name', )
    ordering = ('state_id', 'state_name', )
    # list_filter=['user_type',]





# admin.site.register(State)