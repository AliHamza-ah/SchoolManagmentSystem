from django.urls import path
from Branch.views import *

urlpatterns = [
    path('create_branch/', create_branch, name='create_branch'),
    path('edit_branch/<int:pk>/', edit_branch, name='edit_branch'),
    path('deactivate_branch/<int:pk>/', deactivate_branch, name='deactivate_branch'),
    path('activate_branch/<int:pk>/', activate_branch, name='activate_branch'),
    path('branches/', branches, name='branches'),
]