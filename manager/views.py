from django.shortcuts import render
from .models import *


# Create your views here.


@login_required
def project_list(request):
#    project = Project.objects.filter(created_date__lte=timezone.now())
    project = Project.objects.all()
    return render(request, 'project_list.html',
                  {'projects': project})