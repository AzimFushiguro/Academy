from django.contrib import admin
from apps.users.models import User
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id","full_name","phone_number","avatar")
# Register your models here.
