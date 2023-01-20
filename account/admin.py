from django.contrib import admin
from account.models import User
# Register your models here.

class DontLog:
    def log_addition(self, *args):
        return

@admin.register(User)
class UserAdmin(DontLog, admin.ModelAdmin):
  
    list_display = ('user_id','email', 'first_name', 'last_name', 'user_type', "username", "mobile_number", "created_at")
    search_fields = ('email', 'first_name', 'last_name', 'username', 'created_at')
    ordering = ('user_type','email', 'created_at', )
    list_filter=['user_type',]





# admin.site.register(User)
