from django.contrib import admin
from .models import Student,Teacher,CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Teacher)