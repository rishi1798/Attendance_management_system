from django.contrib import admin
from .models import Users, Departments, Students, Courses, AttendanceLog
# Register your models here.

admin.site.register(Users)
admin.site.register(Departments)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(AttendanceLog)
