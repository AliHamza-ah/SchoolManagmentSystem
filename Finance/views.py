from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


# Create your views here.
@login_required
@permission_required('Finance.view_level1')
def home(request):
    level1 = Level1.objects.all().order_by('id')
    level2 = Level2.objects.all().order_by('code')
    level3 = Level3.objects.all().order_by('code')
    level4 = Level4.objects.all().order_by('code')
    level5 = Level5.objects.all().order_by('code')
    context = {
        'level1': level1,
        'level2': level2,
        'level3': level3,
        'level4': level4,
        'level5': level5,
    }
    return render(request, 'Finance/home.html', context)


@login_required
@permission_required('Finance.add_level1')
def create_level1(request):
    form = Level1Form()
    level1 = Level1.objects.all()
    if request.method == 'POST':
        form = Level1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_level1')
        return render(request, 'Finance/level1.html',
                      {'form': form, 'message': "The level one object of this name already exists."})
    return render(request, 'Finance/level1.html', {'form': form, 'level1': level1})


@login_required
@permission_required('Finance.add_level2')
def create_level2(request):
    form = Level2Form()
    level2 = Level2.objects.all().order_by('code')
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
            return redirect('create_level2')
        return render(request, 'Finance/level2.html',
                      {'form': form, 'message': "The level two object of this name already exists.", 'level2': level2})
    return render(request, 'Finance/level2.html', {'form': form, 'level2': level2})

@permission_required('Finance.edit_level2')
def edit_level2(request, pk):
    level = get_object_or_404(Level2, pk=pk)
    level2 = Level2.objects.all().order_by('code')
    form = Level2Form(instance=level)
    if request.method == 'POST':
        form = Level2Form(request.POST, instance=level)
        form.save()
        return redirect('create_level2')
    context = {
        'form': form,
        'level2': level2,
    }
    return render(request, 'Finance/edit_level2.html', context)


@login_required
@permission_required('Finance.add_level3')
def create_level3(request):
    form = Level3Form()
    level3 = Level3.objects.all().order_by('code')
    if request.method == 'POST':
        form = Level3Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            parent_level = form.cleaned_data.get('parent_level')
            print(form.cleaned_data)
            print(f"parent_level : {parent_level}")
            id_parenet_level = Level2.objects.get(name=parent_level).id
            code_parenet_level = Level2.objects.get(name=parent_level).code
            print(id_parenet_level)
            count = Level3.objects.filter(parent_level_id=id_parenet_level).count()
            print(f"count : {count}")
            obj.code = (int(code_parenet_level) * 1000) + count + 1
            obj.save()
            return redirect('home')
        return render(request, 'Finance/level3.html',
                      {'form': form, 'message': "The level three object of this name already exists.",
                       'level3': level3})
    return render(request, 'Finance/level3.html', {'form': form, 'level3': level3})


def edit_level3(request, pk):
    level = get_object_or_404(Level3, pk=pk)
    level3 = Level3.objects.all().order_by('code')
    form = Level3Form(instance=level)
    if request.method == 'POST':
        form = Level3Form(request.POST, instance=level)
        form.save()
        return redirect('create_level3')
    context = {
        'form': form,
        'level2': level3,
    }
    return render(request, 'Finance/edit_level3.html', context)


@login_required
def create_level4(request):
    form = Level4Form()
    level4 = Level4.objects.all().order_by('code')
    if request.method == 'POST':
        form = Level4Form(request.POST)
        print(form)
        if form.is_valid():
            obj = form.save(commit=False)
            parent_level = form.cleaned_data.get('parent_level')
            print(form.cleaned_data)
            print(f"parent_level : {parent_level}")
            id_parenet_level = Level3.objects.get(name=parent_level).id
            code_parenet_level = Level3.objects.get(name=parent_level).code
            print(id_parenet_level)
            count = Level4.objects.filter(parent_level_id=id_parenet_level).count()
            print(f"count : {count}")
            print("form is valid")
            obj.code = (int(code_parenet_level) * 100000) + count + 1
            obj.save()
            return redirect('create_level4')
        return render(request, 'Finance/level4.html',
                      {'form': form, 'message': "The level Four object of this name already exists.",'level4': level4})
    return render(request, 'Finance/level4.html', {'form': form, 'level4': level4})


def edit_level4(request, pk):
    level = get_object_or_404(Level4, pk=pk)
    level4 = Level4.objects.all().order_by('code')
    form = Level4Form(instance=level)
    if request.method == 'POST':
        form = Level4Form(request.POST, instance=level)
        form.save()
        return redirect('create_level4')
    context = {
        'form': form,
        'level4': level4,
    }
    return render(request, 'Finance/edit_level4.html', context)


def load_level2(request):
    parent_level_id = request.GET.get('parent_level')
    print(parent_level_id)
    level2 = Level2.objects.filter(parent_level__id=parent_level_id)
    print(level2)
    context = {'level2': level2}
    return render(request, 'Finance/level2_dropdown_list_options.html', context)


def load_level3(request):
    parent_level_id = request.GET.get('parent_level')
    level3 = Level3.objects.filter(parent_level__id=parent_level_id)
    print(level3)
    context = {'level3': level3}
    return render(request, 'Finance/level3_dropdown_list_options.html', context)


@login_required
def create_level5(request):
    form = Level5Form()
    if request.method == 'POST':
        form = Level5Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'Finance/level5.html',
                      {'form': form, 'message': "The level one object of this name already exists."})
    return render(request, 'Finance/level5.html', {'form': form})
