from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import *
from .models import Employee, Client, Project
from .forms import *
from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

now = timezone.now()
#Employee
@login_required
def assignment_new(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
#            assignment.created_date = timezone.now()
            assignment.save()
            assignment = Assignment.objects.all
            employee = Employee.objects.all
            email = request.POST.get("email")
            project_name = request.POST.get("project_name")
            project_manager = request.POST.get("Project_manager")
            email = request.POST.get("email")
            subject = 'AK Infotech: Your new Project Assignment!'
            message = f'You have a new Project Assignment Created. Please contact your project Manager for ' \
                      f'further details'
            html_message = render_to_string('employee_assignment.html', {'context': 'values'})
            plain_message = strip_tags(html_message)
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER, email])
            return render(request, 'assignment_list.html',
                          {'assignments': assignment})
    else:
        form = AssignmentForm()
        # print("Else")
    return render(request, 'assignment_new.html', {'form': form})


@login_required
def assignment_list(request):
    #    project = Project.objects.filter(created_date__lte=timezone.now())
    assignment = Assignment.objects.all()
    return render(request, 'assignment_list.html',
                  {'assignments': assignment})


@login_required
def assignment_edit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == "POST":
        # update
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.updated_date = timezone.now()
            assignment.save()
            #            project = Project.objects.filter(created_date__lte=timezone.now())
            assignment = Assignment.objects.all()
            return render(request, 'assignment_list.html',
                          {'assignments': assignment})
    else:
        # edit
        form = AssignmentForm(instance=assignment)
    return render(request, 'assignment_edit.html', {'form': form})


@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.delete()
    return redirect('assignment_list')