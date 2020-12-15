from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('make_user/', make_user, name='make_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('employee_list/', employee_list, name='employee_list'),
    path('employee_detail/<int:pk>/', employee_detail, name='employee_detail'),
    path('edit_designation/<int:pk>/', edit_designation, name='edit_designation'),
    # path('edit_perms/<int:pk>/ajax_add_perms/', ajax_add_perms, name='ajax_add_perms'),
    path('edit_perms/<int:pk>/ajax_rm_perms/', ajax_rm_perms, name='ajax_rm_perms'),
    path('edit_perms/<int:pk>/', edit_perms, name='edit_perms'),
]