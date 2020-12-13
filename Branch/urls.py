from django.urls import path
from Branch.views import *

urlpatterns = [
    path('create_branch/', create_branch, name='create_branch'),
    path('edit_branch/<int:pk>/', edit_branch, name='edit_branch'),
]