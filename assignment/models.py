from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from manager.models import Client, Project, Employee
#from users.models import Customuser
# Create your models here.
import users.models


class Assignment(models.Model):
    employee_name = models.ForeignKey(Employee, related_name='name', blank=False, null=False, default=' ', on_delete=models.CASCADE)
    #    client_id = models.CharField(max_length=50, blank=False, null=False, default=' ')
    allocation_percentage = models.IntegerField(blank=False, null=False, default=' ')
    Project_manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_name = models.ForeignKey(Project, related_name='client', max_length=50, blank=False,
                                     null=False, default=' ',
                                     on_delete=models.DO_NOTHING)
    comments = models.CharField(max_length=50, blank=False, null=False, default=' ')

    def __int__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])
