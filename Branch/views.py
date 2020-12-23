from django.shortcuts import render, redirect, get_object_or_404
from Accounts.models import Employee
from .models import Branch
from .forms import BranchForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def create_branch(request):
    form = BranchForm()
    branches = Branch.objects.all().order_by('id')
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_branch')
        return render(request, 'Branch/create_branch.html',
                      {'form': form, 'message': "The level one object of this name already exists.",
                       'branches': branches})
    return render(request, 'Branch/create_branch.html', {'form': form, 'branches': branches})


@user_passes_test(lambda u: u.is_superuser)
def edit_branch(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    branches = Branch.objects.all().order_by('name')
    form = BranchForm(instance=branch)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        form.save()
        return redirect('create_branch')
    context = {
        'form': form,
        'branches': branches,
    }
    return render(request, 'Branch/edit_branch.html', context)

@user_passes_test(lambda u: u.is_superuser)
def branches(request):
    branches = Branch.objects.all().order_by("name")
    return render(request, 'Branch/branches.html', {'branches': branches})

@user_passes_test(lambda u: u.is_superuser)
def deactivate_branch(request, pk):
    branch = Branch.objects.get(pk=pk)
    branch.is_active = False
    branch.save()

    employees = Employee.objects.filter(branch=branch)

    for employee in employees:
        employee.user.is_active = False
        employee.user.save()
    return redirect('branches')

@user_passes_test(lambda u: u.is_superuser)
def activate_branch(request, pk):
    branch = Branch.objects.get(pk=pk)
    branch.is_active = True
    branch.save()
    employees = Employee.objects.filter(branch=branch)

    for employee in employees:
        employee.user.is_active = True
        employee.user.save()
    return redirect('branches')
