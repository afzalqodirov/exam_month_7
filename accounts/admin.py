from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'is_reviewer', 'is_staff')
    search_fields = ('first_name', 'last_name', 'username')

admin.site.register(CustomUser, CustomUserAdmin)
