from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import *


# Create your views here.
def student_home(request):
    pass


def student_registration(request):
    student_form = StudentForm(request.POST or None)

    if request.method == "POST":
        if student_form.is_valid():
            student_form.save(commit=False)
            student_form.save()
            return redirect('student-list')
    context = {
        'student_form': student_form,
    }
    return render(request, 'Student/student-registration.html', context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'Student/student-detail.html', {'student': student})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'Student/student_list.html', {'students': students})

def student_session_list(request, academic_year):
    students = get_list_or_404(Student, cls__academic_year__start_year__exact = academic_year)
    return render(request, 'Student/student_session_list.html', {'students': students})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    student_form = StudentForm(instance=student)
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save(commit=False)
            student_form.save()
            return redirect('student-list')
        return render(request, 'Student/student-edit.html', {'student_form': student_form, 'message': "Data invalid"})
    else:
        return render(request, 'Student/student-edit.html',
                      {'student_form': student_form, 'message': 'Edit the fields'})


def student_contact_list(request):
    students = Student.objects.all()
    return render(request, 'Student/student_contact_list.html', {'students': students})
