from django.shortcuts import render, redirect, get_object_or_404
from .models import Branch
from .forms import BranchForm


# Create your views here.
def create_branch(request):
    form = BranchForm()
    branches = Branch.objects.all().order_by('id')
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_branch')
        return render(request, 'Branch/create_branch.html',
                      {'form': form, 'message': "The level one object of this name already exists.", 'branches': branches})
    return render(request, 'Branch/create_branch.html', {'form': form, 'branches': branches})

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
