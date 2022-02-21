from django.contrib import admin

# Register your models here.


from .models import Project, Employee


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_ID', 'project_description', 'start_date', 'end_date', 'client_name',
                    'client_id', 'SOW_no', 'total_headcount', 'manager']
    list_filter = ['project_name', 'client_name', 'manager']
    list_editable = ['manager', 'client_name', 'start_date', 'end_date']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'employee_ID', 'first_name', 'last_name', 'Email', 'DOJ',
                    'Project_manager', 'Location', 'Designation']
    list_filter = ['employee_name', 'Location', 'Project_manager', 'Designation']
    list_editable = ['Email', 'Location']
