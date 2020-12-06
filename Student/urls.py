from django.urls import path
from .views import *

urlpatterns = [
    path('student-registration', student_registration, name='student-registration'),
    path('student-list', student_list, name='student-list'),
    path('<int:pk>', student_detail, name='student-detail'),
    path('edit/<int:pk>', student_edit, name='student-edit'),


]