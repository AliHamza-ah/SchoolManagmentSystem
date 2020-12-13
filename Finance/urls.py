from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('create_level1/', create_level1, name='create_level1'),
    path('create_level2/', create_level2, name='create_level2'),
    path('edit_level2/<int:pk>/', edit_level2, name='edit_level2'),
    path('create_level3/', create_level3, name='create_level3'),
    path('edit_level3/<int:pk>', edit_level3, name='edit_level3'),
    path('create_level4/', create_level4, name='create_level4'),
    path('edit_level4/<int:pk>', edit_level4, name='edit_level4'),
    path('create_level5/', create_level5, name='create_level5'),
    path('ajax/load-level2/', load_level2, name='ajax_load_level2'),
    path('ajax/load-level3/', load_level3, name='ajax_load_level3'),
    # path('level1/<int:pk>/level2', create_level2, name='create_level2'),
    # path('level1/level2/<int:pk>/level3/', create_level3, name='create_level3'),
    # path('level1/level2/level3/level4', create_level4, name='create_level4'),
]
