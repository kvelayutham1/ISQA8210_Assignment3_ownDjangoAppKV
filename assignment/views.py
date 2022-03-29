from django.shortcuts import render, redirect
from .models import *
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