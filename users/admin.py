from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'department', 'cell_phone', 'is_staff', 'date_of_joining', 'employee_ID',
                    'first_name', 'last_name',]


admin.site.register(CustomUser, CustomUserAdmin)