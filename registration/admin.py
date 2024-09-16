from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)  # Register the custom User admin
