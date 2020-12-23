from django.contrib import admin
from .models import *


# Register your models here
class Level1Admin(admin.ModelAdmin):
    list_display = ['name', 'id']
    list_filter = ['name', 'id']
    search_fields = ['name__icontains']


admin.site.register(Level1, Level1Admin)


class Level2Admin(admin.ModelAdmin):
    list_display = ['name', 'parent_level', 'code']
    list_filter = ['name', 'parent_level', 'code']
    search_fields = ['name__icontains']


admin.site.register(Level2, Level2Admin)


class Level3Admin(admin.ModelAdmin):
    list_display = ['name', 'parent_level', 'parent_level1', 'code']
    list_filter = ['name', 'parent_level', 'parent_level1', 'code']
    search_fields = ['name__icontains']


admin.site.register(Level3, Level3Admin)

class Level4Admin(admin.ModelAdmin):
    list_display = ['name', 'parent_level','parent_level2', 'parent_level1', 'code']
    list_filter = ['name', 'parent_level', 'parent_level2','parent_level1', 'code']
    search_fields = ['name__icontains']


admin.site.register(Level4, Level4Admin)
admin.site.register(FinancialYear)
admin.site.register(OpeningBalance)


