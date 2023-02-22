from django.shortcuts import redirect
from user.models import Student

def adminonly(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff or request.user.user_type == 'Admin':
                return(function(request, *args, **kwargs))
            else:
                return redirect('404')
        else:
            return redirect('404')
    return wrapper

def teacheronly(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == "Teacher" or request.user.is_staff:
                return(function(request, *args, **kwargs))
            else:
                return redirect('404')
        else:
            return redirect('404')
    return wrapper

def studentonly(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == "Student" or request.user.is_staff:
                return(function(request,*args,**kwargs))
            else:
                return redirect('404')
        else:
            return redirect('404')
    return wrapper