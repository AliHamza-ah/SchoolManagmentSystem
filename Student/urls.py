from django.urls import path
from .views import *

urlpatterns = [

    path('', student_home, name='student-home'),
    path('student-registration', student_registration, name='student-registration'),
    path('student-list', student_list, name='student-list'),
    path('student-session-list/<int:academic_year>', student_session_list, name='student_session_list'),
    path('student-contact-list', student_contact_list, name='student-contact-list'),
    path('<int:pk>', student_detail, name='student-detail'),
    path('edit/<int:pk>', student_edit, name='student-edit'),
]