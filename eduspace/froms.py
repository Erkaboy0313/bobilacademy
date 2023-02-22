from django import forms

from teaching.models import Group, GroupModul, GroupTheme
from .models import Sugession,Course,Module,Register
from user.models import CustomUser, Teacher
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Sugession
        fields = ['first_name','last_name','phone','subject','body']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','image','price','desciption']

class ModulForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','first_name','last_name','phone','password1','password2']

class TeacherForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','first_name','last_name','phone','password1','password2']

class AdminForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','first_name','last_name','phone','user_type','password1','password2']

class UserupdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','phone','password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
    
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name','teacher','students','image']

class GroupModulFrom(forms.ModelForm):
    class Meta:
        model = GroupModul
        fields = ['name','image']

class GroupThemeForm(forms.ModelForm):
    class Meta:
        model = GroupTheme
        fields = ['name','file','task','video']