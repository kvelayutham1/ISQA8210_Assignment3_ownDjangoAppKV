from django.contrib import admin

# Register your models here.

from .models import Assignment


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'allocation_percentage', 'Project_manager', 'start_date', 'end_date',
                    'project_name', 'comments']
    list_filter = ['employee_name', 'project_name', 'Project_manager']
    list_editable = ['allocation_percentage', 'project_name', 'Project_manager']
