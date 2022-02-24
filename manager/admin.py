from django.contrib import admin

# Register your models here.


from .models import Project, Employee, Client


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_description', 'start_date', 'end_date', 'client_name',
                    'SOW_no', 'total_headcount', 'manager']
    list_filter = ['project_name', 'client_name', 'manager']
    list_editable = ['manager', 'client_name', 'start_date', 'end_date']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'first_name', 'last_name', 'Email', 'DOJ',
                    'Project_manager', 'Location', 'Designation']
    list_filter = ['employee_name', 'Location', 'Project_manager', 'Designation']
    list_editable = ['Email', 'Location']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'POC_client', 'POC_manager']
    list_filter = ['client_name', 'POC_client', 'POC_manager']
    list_editable = ['POC_client', 'POC_manager']
