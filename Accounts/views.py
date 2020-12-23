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
            if request.user.is_superuser:
                employee = Employee.objects.create(user=user, branch=None)
                user.save()
                employee.save()
                return redirect('make_employee')
            else:
                employee = Employee.objects.create(user=user, branch=request.user.employee.branch)
                user.save()
                employee.save()
                return redirect('employee_list')
        return render(request, 'accounts/make_user.html', {'form': form, 'message': 'Invalid Data'})
    return render(request, 'accounts/make_user.html', {'form': form})


def users(request):
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        employees = Employee.objects.filter(branch=request.user.employee.branch).values('user__pk')
        users = User.objects.filter(pk__in=employees).exclude(pk=request.user.pk)
    return render(request, 'Accounts/users.html', {'users': users})


def deactivate_user(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect('users')


def activate_user(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect('users')


def make_employee(request):
    form = EmployeeForm()
    if request.user.is_superuser:
        if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('employee_list')
        return render(request, 'Finance/make_employee.html', {'form': form})
    return render(request, 'Finance/make_employee.html', {'form': form})


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
    user_perms = user.user_permissions.all()
    if request.user.is_superuser:
        manager_perms = Permission.objects.all()
    else:
        manager_perms = manager.user_permissions.all()

    # complementing Manger's QuerySet to Show only not assigned permissions
    manager_perms = manager_perms.exclude(pk__in=user_perms.values_list('pk', flat=True))
    manger_form = PermissionSelectForm(queryset=manager_perms, nm="manager_form")
    user_form = PermissionSelectForm(queryset=user_perms, nm="user_form")
    # print(manager_perms)
    if request.method == 'POST':
        use_perms = request.POST.getlist('user_form')
        man_perms = request.POST.getlist('manager_form')
        print(use_perms)
        print(man_perms)
        u_p = [user_perm.id for user_perm in user_perms]
        for perm in man_perms:
            user.user_permissions.add(int(perm))
        for perm in use_perms:
            user.user_permissions.remove(int(perm))
        user.save()
    context = {
        'manger_form': manger_form,
        'user_form': user_form,
        'pk': pk,
    }
    return render(request, 'Accounts/user_perms.html', context=context)


def ajax_rm_perms(request):
    print(request.POST['user_permissions'])
    print(request.POST['pk'])
    return HttpResponse()


def edit_designation(request, pk):
    pass


def edit_permissions(request, pk):
    pass
