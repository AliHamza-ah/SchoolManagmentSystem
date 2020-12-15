from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Employee)
admin.site.register(Class)
admin.site.register(Section)
# admin.site.register(Fee)
admin.site.register(Academic_Session)
admin.site.register(Religion)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)



class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'cls']
    list_filter = ['name', 'cls']
    search_fields = ['name__icontains']

admin.site.register(Student, StudentAdmin)
