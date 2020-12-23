from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from itertools import chain
from datetime import datetime


# Create your views here.
@login_required
@permission_required('Finance.view_level1')
def home(request):
    """
    :param request:
    :return:
    """
    level1 = Level1.objects.all()
    level2 = Level2.objects.all()
    level3 = Level3.objects.all()
    level4 = Level4.objects.all()
    level = sorted(chain(level1, level2, level3, level4), key=lambda x: str(x.code))
    return render(request, 'Finance/home.html', {"level": level})


@login_required
@permission_required('Finance.add_level1')
def create_level1(request):
    """

    :param request:
    :return:
    """
    form = Level1Form()
    level1 = Level1.objects.all().filter(is_active=True)
    if request.method == 'POST':
        form = Level1Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.code = Level1.objects.all().count() + 1
            form.save()
            return redirect('home')
        return render(request, 'Finance/level1.html',
                      {'form': form, 'message': "The level one object of this name already exists."})
    return render(request, 'Finance/level1.html', {'form': form, 'level1': level1})


def edit_level1(request, pk):
    level = get_object_or_404(Level1, pk=pk)
    level1 = Level1.objects.all().order_by('code').filter(is_active=True)
    form = Level1Form(instance=level)
    if request.method == 'POST':
        form = Level1Form(request.POST, instance=level)
        form.save()
        return redirect('home')
    context = {
        'form': form,
        'level1': level1,
    }
    return render(request, 'Finance/edit_level1.html', context)


@login_required
@permission_required('Finance.add_level2')
def create_level2(request):
    """

    :param request:
    :return:
    """
    form = Level2Form()
    level2 = Level2.objects.all().order_by('code').filter(is_active=True)
    if request.method == 'POST':
        form = Level2Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            parent_level = form.cleaned_data.get('parent_level')
            print(parent_level)
            id_parenet_level = Level1.objects.get(name=parent_level).pk
            print(id_parenet_level)
            obj.code = (int(id_parenet_level) * 100) + Level2.objects.filter(
                parent_level__id=id_parenet_level).count() + 1
            obj.save()
            return redirect('home')
        return render(request, 'Finance/level2.html',
                      {'form': form, 'message': "The level two object of this name already exists.", 'level2': level2})
    return render(request, 'Finance/level2.html', {'form': form, 'level2': level2})


@permission_required('Finance.edit_level2')
def edit_level2(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    level = get_object_or_404(Level2, pk=pk)
    level2 = Level2.objects.all().order_by('code').filter(is_active=True)
    form = Level2Form(instance=level)
    if request.method == 'POST':
        form = Level2Form(request.POST, instance=level)
        form.save()
        return redirect('home')
    context = {
        'form': form,
        'level2': level2,
    }
    return render(request, 'Finance/edit_level2.html', context)


@login_required
@permission_required('Finance.add_level3')
def create_level3(request):
    """

    :param request:
    :return:
    """
    form = Level3Form()
    level3 = Level3.objects.all().order_by('code').filter(is_active=True)
    if request.method == 'POST':
        form = Level3Form(request.POST)
        print(form)
        if form.is_valid():
            obj = form.save(commit=False)
            parent_level = form.cleaned_data.get('parent_level')
            id_parent_level = Level2.objects.get(name=parent_level).id
            code_parent_level = Level2.objects.get(name=parent_level).code
            count = Level3.objects.filter(parent_level_id=id_parent_level).count()
            obj.code = (int(code_parent_level) * 1000) + count + 1
            obj.save()
            return redirect('home')
        return render(request, 'Finance/level3.html',
                      {'form': form, 'message': "Couldn't Create Level 3 an error has occurred",
                       'level3': level3})
    return render(request, 'Finance/level3.html', {'form': form, 'level3': level3})


@login_required
@permission_required('Finance.edit_level3')
def edit_level3(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    level = get_object_or_404(Level3, pk=pk)
    level3 = Level3.objects.all().order_by('code').filter(is_active=True)
    form = Level3Form(instance=level)
    if request.method == 'POST':
        form = Level3Form(request.POST, instance=level)
        form.save()
        return redirect('home')
    context = {
        'form': form,
        'level3': level3,
    }
    return render(request, 'Finance/edit_level3.html', context)


@login_required
@permission_required('Finance.add_level4')
def create_level4(request):
    """

    :param request:
    :return:
    """
    form = Level4Form()
    level4 = Level4.objects.all().order_by('code').filter(is_active=True)
    if request.method == 'POST':
        form = Level4Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            parent_level = form.cleaned_data.get('parent_level')
            id_parenet_level = Level3.objects.get(name=parent_level).id
            code_parenet_level = Level3.objects.get(name=parent_level).code
            count = Level4.objects.filter(parent_level_id=id_parenet_level).count()
            obj.code = (int(code_parenet_level) * 100000) + count + 1
            obj.save()
            return redirect('home')
        return render(request, 'Finance/level4.html',
                      {'form': form, 'message': "The level Four object of this name already exists.", 'level4': level4})
    return render(request, 'Finance/level4.html', {'form': form, 'level4': level4})


@login_required
@permission_required('Finance.change_level4')
def edit_level4(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    level = get_object_or_404(Level4, pk=pk)
    level4 = Level4.objects.all().order_by('code').filter(is_active=True)
    form = Level4Form(instance=level)
    if request.method == 'POST':
        form = Level4Form(request.POST, instance=level)
        form.save()
        return redirect('home')
    context = {
        'form': form,
        'level4': level4,
    }
    return render(request, 'Finance/edit_level4.html', context)


def load_level2(request):
    """

    :param request:
    :return:
    """
    parent_level_id = request.GET.get('parent_level')
    level2 = Level2.objects.filter(parent_level__id=parent_level_id).filter(is_active=True)
    context = {'level2': level2}
    return render(request, 'Finance/level2_dropdown_list_options.html', context)


def load_level3(request):
    """

    :param request:
    :return:
    """
    parent_level_id = request.GET.get('parent_level')
    level3 = Level3.objects.filter(parent_level__id=parent_level_id).filter(is_active=True)
    context = {'level3': level3}
    return render(request, 'Finance/level3_dropdown_list_options.html', context)

@login_required
@permission_required('Finance.add_financialyear')
def add_financial_year(request):
    """

    :param request:
    :return:
    """
    form = FinancialYearForm()
    if request.method == "POST":
        form = FinancialYearForm(request.POST)
        year_status_check = FinancialYear.objects.filter(is_active=True)
        if len(year_status_check) != 0:
            return render(request, 'Finance/create_financial_year.html',
                          {'form': form, "message": "An Year is already active can't create another year"})
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.branch = request.user.employee.branch
                obj.save()
                return redirect('financial_years')
        return render(request, 'Finance/create_financial_year.html', {'form': form})
    return render(request, 'Finance/create_financial_year.html', {'form': form})

@login_required
@permission_required('Finance.change_financialyear')
def edit_financial_year(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    year = get_object_or_404(FinancialYear, pk=pk)
    form = FinancialYearForm(instance=year)
    if request.method == 'POST':
        form = FinancialYearForm(request.POST, instance=year)
        request_status = request.POST.get('is_active')
        status_check = FinancialYear.objects.filter(is_active=True)
        if request_status and (len(status_check) > 0):
            return render(request, 'Finance/edit_financial_year.html',
                          {'form': form, "message": "An Year is already active can't make another year active"})
        else:
            form.save()
            return redirect('financial_years')
    context = {
        'form': form,
    }
    return render(request, 'Finance/edit_financial_year.html', context)

@login_required
@permission_required('Finance.view_financialyear')
@permission_required('Finance.change_financialyear')
def financial_years(request):
    """

    :param request:
    :return:
    """
    years = FinancialYear.objects.all()
    return render(request, 'Finance/financial_years.html', {'years': years})

@login_required
@permission_required('Finance.add_openingbalance')
def add_opening_balance(request):
    """

    :param request:
    :return:
    """
    form = OpeningBalanceForm()
    financial_year = FinancialYear.objects.get(is_active=True)
    qs = OpeningBalance.objects.filter(branch=request.user.employee.branch).filter(year=financial_year).values(
        'account_name')
    form.fields['account_name'].queryset = Level4.objects.exclude(id__in=qs)
    if request.method == "POST":
        form = OpeningBalanceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.branch = request.user.employee.branch
            obj.year = FinancialYear.objects.get(is_active=True)
            obj.save()
            return redirect('dashboard')
        return render(request, 'Finance/create_opening_balance.html', {'form': form})
    return render(request, 'Finance/create_opening_balance.html', {'form': form})
@login_required
@permission_required('Finance.view_openingbalance')
def opening_balance(request):
    """

    :param request:
    :return:
    """
    balance = OpeningBalance.objects.filter(year__start_date__year=datetime.now().year)
    form = OpeningBalanceInquiryForm()
    if request.method == "POST":
        date = request.POST.get('year')
        print(date)
        year = FinancialYear.objects.get(id=date)
        date = year.end_date.year
        balance = OpeningBalance.objects.filter(year__end_date__year=date)
    return render(request, 'Finance/opening_balance.html', {"balance": balance, "form": form})
