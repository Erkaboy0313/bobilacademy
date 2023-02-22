from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from django.contrib import messages
# Create your views here.


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        if user:
            login(request=request,user=user)
            user = CustomUser.objects.get(username = username)
            if user.is_staff or user.user_type == 'Admin':
                return redirect('dashboard')
            elif user.user_type == 'Student':
                return redirect('mycourses')
            elif user.user_type == 'Teacher':
                return redirect('my_groups')
        else:
            messages.add_message(request,messages.WARNING,'Foydalanuvchi topilmadi')
    return render(request,'main/login.html')
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')