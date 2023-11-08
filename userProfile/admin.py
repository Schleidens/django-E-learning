from django.contrib import admin

from .models import studentProfile, teacherProfile

# Register your models here.

admin.site.register(studentProfile)
admin.site.register(teacherProfile)
