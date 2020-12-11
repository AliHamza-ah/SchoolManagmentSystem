from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
@login_required
@permission_required('add.Finance', raise_exception=True)
def home(request):
    return render(request, 'Finance/home.html')

@login_required
@permission_required('add.Finance', raise_exception=True)
def create_level1(request):
    form = Level1Form()
    if request.method == 'POST':
        form = Level1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'Finance/level1.html',
                      {'form': form, 'message': "The level one object of this name already exists."})
    return render(request, 'Finance/level1.html', {'form': form})

@login_required
@permission_required('add.Finance', raise_exception=True)
def create_level2(request):
    form = Level2Form()
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
                      {'form': form, 'message': "The level two object of this name already exists."})
    return render(request, 'Finance/level2.html', {'form': form})


@login_required
@permission_required('add.Finance', raise_exception=True)
def create_level3(request):
    form = Level3Form()
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
                      {'form': form, 'message': "The level three object of this name already exists."})
    return render(request, 'Finance/level3.html', {'form': form})


@login_required
@permission_required('add.Finance', raise_exception=True)
def create_level4(request):
    form = Level4Form()
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
            obj.code = (int(code_parenet_level) * 10000) + count + 1
            obj.save()
            return redirect('home')
        return render(request, 'Finance/level4.html',
                      {'form': form, 'message': "The level Four object of this name already exists."})
    return render(request, 'Finance/level4.html', {'form': form})


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
@permission_required('add.Finance', raise_exception=True)
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
