from django.shortcuts import render
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404
from .forms import *
from .models import *
from Finance.models import *
from Finance.forms import *


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            return render(request, 'Accounts/login.html', {'form': form, 'message': 'Invalid Details'})
    else:
        return render(request, 'Accounts/login.html', {'form': form})


def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('login_user')


def make_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            employee = Employee.objects.create(user=user, branch=request.user.employee.branch)
            user.save()
            employee.save()
            return redirect('employee_list')
        return render(request, 'accounts/make_user.html', {'form': form, 'message': 'Invalid Data'})
    return render(request, 'accounts/make_user.html', {'form': form})


def employee_list(request):
    if request.user.is_superuser:
        employees = Employee.objects.all()
    else:
        employees = Employee.objects.filter(branch=request.user.employee.branch).order_by('user__username')
    return render(request, 'Accounts/employee_list.html', {'employees': employees})


def employee_detail(request, pk):
    employees = Employee.objects.get(pk=pk)
    return render(request, 'Accounts/employee_detail.html', {'employees': employees})


def edit_perms(request, pk):
    if request.user.is_superuser:
        user = Employee.objects.get(pk=pk).user
        manager = User.objects.get(username=request.user)
    else:
        user = Employee.objects.filter(branch=request.user.employee.branch).get(pk=pk).user
        manager = Employee.objects.filter(branch=request.user.employee.branch).get(user=request.user).user
    if user is None:
        return Http404
    if request.method == 'POST':
        perms = request.POST.getlist('user_permissions')
        print(perms)
        # for perm in perms:
        #     user.user_permissions.add(int(perm))
        # user.save()
    user_perms = user.user_permissions.all()
    if request.user.is_superuser:
        manager_perms = Permission.objects.all()
    else:
        manager_perms = manager.user_permissions.all()
    context = {
        'manager_perms': manager_perms,
        'user_perms': user_perms,
    }
    return render(request, 'Accounts/user_perms.html', context=context)


def edit_designation(request, pk):
    pass


def edit_permissions(request, pk):
    pass
