from django.http import  HttpResponseRedirect
from django.shortcuts import redirect, render
from teaching.models import Group, GroupModul, GroupTheme, Payment
from .models import Course,Module, Project, Sugession,Theme,News,AboutUs,Register
from user.models import CustomUser, Teacher,Student
from .froms import ContactForm,CourseForm, GroupForm,LoginForm, ModulForm,UserForm,TeacherForm,UserupdateForm,RegisterForm,GroupThemeForm,GroupModulFrom,AdminForm
from django.contrib import messages
from .decorators import adminonly, teacheronly
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.http.response import JsonResponse
from django.contrib.auth import authenticate,login
import json
courcess = {
    1:"frond",
    2:"back",
    3:"android",
    4:"english",
    5:"flutter",
    6:"3dmax",
    7:"comp",
    8:"rus",
    9:"arab",
    10:"math",
    11:"mental",
    12:"school"}

def register_course(request):
    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Muvofiqiyatli ro'yxatdan o'tdingiz.!!! Adminlarimiz tez orada siz bilan bog'lanishadi.") 
        else:
            messages.add_message(request,messages.ERROR,"Ro'yxatdan o'tishda xato yuz berdi") 
        print(url)
        if 'register' in url:
            return redirect('index')
        else:
            return redirect(url)
    return render(request,'main/register.html')

def error(request):
    return render(request,'dashboard/pages/error-404.html')

def sugessions(request):
    suggessions = Sugession.objects.all()

    context = {
        'sugessions':suggessions
    }
    return render(request,'dashboard/sugessions.html',context)

def index(request):
    courses = Course.objects.all()
    projects = Project.project.tottal_projects()
    teachers = Teacher.objects.all()
    students = Student.student.tottal_students()
    context = {
        'courses':courses,
        'projects':projects,
        'teachers':teachers,
        'students':students
    }
    return render(request,'main/index.html',context)
def courses(request):
    return render(request,'main/courses.html')
def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            phone = request.POST.get('phone')
            if phone.startswith('+'):
                phone = phone[1::]
            if len(phone) == 12 and phone.isdigit():
                form.save()
                messages.add_message(request,messages.SUCCESS,"Habar muvoffaqiyatli yuborildi. Adminlarimiz siz bilan tez orada bog'lanishadi.")      
            else:
                messages.add_message(request,messages.ERROR,"No to'g'ri malumotlar kiritdingiz. Iltimos tekshirib ko'rib qaytadan urinib ko'ring")      
        else:
            messages.add_message(request,messages.ERROR,"No to'g'ri malumotlar kiritdingiz. Iltimos tekshirib ko'rib qaytadan urinib ko'ring")      
    return render(request,'main/contacts.html')
def about(request):
    return render(request,'main/about.html')
def course_type(request,id):
    return render(request,f'main/courses/{courcess[id]}.html')

def log_in(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request,username=username,password=password)
            if user:
                login(request=request,user=user)
                redirect('index')
            else:
                messages.add_message(request,messages.WARNING,"Username yoki Parol noto'g'ri kiritildi")
                HttpResponseRedirect(url)
        else:
            messages.add_message(request,messages.WARNING,"Username yoki Parol noto'g'ri kiritildi")
            HttpResponseRedirect(url)

#------------------------------- Dashboard part begins here --------------------------------

@adminonly
def dashboard(request):
    students = Student.student.tottal_students()
    teachers = Teacher.teacher.tottal_teachers()
    payment = Payment.payment.tottal_payment()
    courses = Course.course.tottal_courses()
    context = {
        'students':students,
        'teachers':teachers,
        'payment':payment,
        'courses':courses
    }
    return render(request,'dashboard/admin.html',context=context)

@adminonly
def course(request):
    if request.method == "POST":
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request,messages.WARNING,'Some thing went wrong')
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request,'dashboard/course.html',context)


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name','image','price','desciption']
    template_name = 'dashboard/dashboardupdate.html'

    def get_object(self):
        return super().get_object()

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data()
        return context
    success_url = '/dashboard/course/'

@adminonly
def removecourse(request):
    data = json.loads(request.body)
    Course.objects.get(id = data['id']).delete()
    return JsonResponse({'message':'success'})

@adminonly
def modul(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = ModulForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request,messages.WARNING,'Some thing went wrong')
            HttpResponseRedirect(url)
    courses = Course.objects.all()
    moduls = Module.objects.all()
    context = {
        'courses':courses,
        'moduls':moduls
    }
    return render(request,'dashboard/modul.html',context=context)


class ModuleUpdateView(UpdateView):
    model = Module
    fields = '__all__'
    template_name = 'dashboard/dashboardupdate.html'

    def get_object(self):
        return super().get_object()

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data()
        return context
    success_url = '/dashboard/modul/'

@adminonly
def removemodule(request):
    data = json.loads(request.body)
    Module.objects.get(id = data['id']).delete()
    return JsonResponse({'message':'success'})

@adminonly
def payment(request):
    if request.method == "POST":
        username = request.POST.get('student')
        group = request.POST.get('group')
        amount = request.POST.get('summa')
        student = Student.objects.get(user__username = username)
        group = Group.objects.get(name = group)
        Payment.objects.create(student=student,group=group,amount=amount)
    students = Student.objects.all()
    groups = Group.objects.all()
    context = {
        'students':students,
        'groups':groups
    }
    return render(request,'dashboard/payment.html',context=context)

@adminonly
def statistics(request):
    return render(request,'dashboard/statistics.html')

@adminonly
def payment_history(request):
    payments = Payment.objects.all()
    context = {
        'payments':payments
    }
    return render(request, 'dashboard/payment_history.html',context=context)

@adminonly
def student(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = CustomUser.objects.get(username = form.cleaned_data.get('username'))
            Student.objects.create(user = user)
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    students = Student.objects.all()
    form = UserForm()
    context = {
        'students':students,
        'form':form
    }
    return render(request,'dashboard/student.html',context)


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['bio','image','free_months']
    template_name = 'dashboard/dashboardupdate.html'

    def get_object(self):
        return super().get_object()

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data()
        user = self.get_object().user
        context['user_form']=UserupdateForm(instance=user)
        return context
    
    def post(self,request,*args,**kwargs):
        user = self.get_object().user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.set_password(request.POST.get('password'))
        try:
            user.save()
        except Exception as e:
            messages.add_message(request,messages.WARNING,e)
        return super().post(request,*args,**kwargs)
    success_url = '/dashboard/student/'

@adminonly
def block_student(request):
    data = json.loads(request.body)
    status = Student.objects.get(id = data['id']).block_user
    return JsonResponse({'status':status})

@adminonly
def removeuser(request):
    data = json.loads(request.body)
    CustomUser.objects.get(id = data['id']).delete()
    return JsonResponse({'message':'success'})


@adminonly
def teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = CustomUser.objects.get(username = form.cleaned_data.get('username'))
            user.user_type = user.TEACHER
            user.save()
            specialization = request.POST.get('specialization')
            Teacher.objects.create(user = user,specialization = specialization)
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    teachers = Teacher.objects.all()
    form = TeacherForm()
    context = {
        'teachers':teachers,
        'form':form
    }
    return render(request,'dashboard/teacher.html',context)


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['bio','image','specialization']
    template_name = 'dashboard/dashboardupdate.html'

    def get_object(self):
        return super().get_object()

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data()
        user = self.get_object().user
        context['user_form']=UserupdateForm(instance=user)
        return context
    
    def post(self,request,*args,**kwargs):
        user = self.get_object().user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.set_password(request.POST.get('password'))
        try:
            user.save()
        except Exception as e:
            messages.add_message(request,messages.WARNING,e)
        return super().post(request,*args,**kwargs)

    success_url = '/dashboard/teacher/'

@adminonly
def news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        try:
            News.objects.create(title=title, image=image,description=description)
        except:
            pass
    new = News.objects.all()
    return render(request, 'dashboard/news.html', {'news':new})

@adminonly
def removenews(request):
    id = json.loads(request.body)['id']
    News.objects.get(id=id).delete()
    return JsonResponse({'data':'deleted'})


class NewsUpdateView(UpdateView):
    model = News
    fields = '__all__'
    template_name = 'dashboard/dashboardupdate.html'
    success_url = '/dashboard/news/'

@adminonly
def change_status(request):
    data = json.loads(request.body)
    news = News.objects.get(id = data['id'])
    if news.status:
        news.status = False
        news.save()
        return JsonResponse({'status':False})
    else:
        news.status = True
        news.save()
        return JsonResponse({'status':True})
@adminonly
def sugession_status(request):
    data = json.loads(request.body)
    news = Sugession.objects.get(id = data['id'])
    if news.status:
        news.status = False
        news.save()
        return JsonResponse({'status':False})
    else:
        news.status = True
        news.save()
        return JsonResponse({'status':True})

@adminonly
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request,messages.WARNING,'Some Thing Went Wrong')
    reg_user = Register.objects.all() 
    context = {
        'registers':reg_user
    }
    return render(request,'dashboard/register.html',context = context)

@adminonly
def reomoveRegister(request):
    data = json.loads(request.body)
    Register.objects.get(id = data['id']).delete()
    return JsonResponse({'status':'ok'})

@adminonly
def group(request):
    groups = Group.objects.all()
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'groups':groups,
        'form':form
    }
    return render(request,'dashboard/group.html',context=context)


class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name','teacher','students','image','cost']
    template_name = 'dashboard/dashboardupdate.html'

    def get_object(self):
        return super().get_object()

    success_url = '/dashboard/group/'

def reomoveGroup(request):
    data = json.loads(request.body)
    Group.objects.get(id = data['id']).delete()
    return JsonResponse({'status':'ok'})

def addAdmin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request,messages.WARNING,'Some thing went wrong')
        return redirect('admins')
    else:
        form = AdminForm()
        admins = CustomUser.objects.filter(user_type = CustomUser.ADMIN)
        return render(request,'dashboard/Addadmin.html',context={'form':form,'admins':admins})


class AdminUpdateView(UpdateView):
    model = CustomUser
    fields = ['first_name','last_name','phone','password']
    template_name = 'dashboard/dashboardupdate.html'
    def post(self,request,*args,**kwargs):
        user = self.get_object()
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.set_password(request.POST.get('password'))
        user.save()
        return redirect('admins')
    success_url = '/dashboard/admins/'

@adminonly
def removeadmin(request):
    id = json.loads(request.body)['id']
    CustomUser.objects.get(id=id).delete()
    return JsonResponse({'data':'deleted'})

#________________________________TeacherPart_____________________________

@teacheronly
def teacher_group(request):
    if request.user.user_type == "Teacher":
        teacher = Teacher.objects.get(user = request.user)
        groups = teacher.group_set.all()
    else:
        groups = Group.objects.all()

    themefrom = GroupThemeForm()
    modulfrom = GroupModulFrom()

    if request.method == "POST":
        if 'addmodul' in request.POST:
            form = GroupModulFrom(request.POST, request.FILES)
            if form.is_valid():
                id = request.POST.get('group')
                group = Group.objects.get(id = id)
                obj = form.save()
                obj.group = group
                obj.save()
                
        elif 'addtheme' in request.POST:
            form = GroupThemeForm(request.POST, request.FILES)
            print(request.FILES)
            if form.is_valid():
                id = request.POST.get('modul')
                modul = GroupModul.objects.get(id = id)
                obj = form.save()
                obj.modul = modul
                obj.save()

    context = {
        'groups':groups,
        'themeform':themefrom,
        'modulform':modulfrom
    }

    return render(request,'teacher_dashboard/group.html', context=context)

class GroupModulUpdateView(UpdateView):
    model = GroupModul
    fields = ['name','image']
    template_name = 'teacher_dashboard/update.html'
    success_url = '/dashboard/teacher_groups/'

class GroupThemeUpdateView(UpdateView):
    model = GroupTheme
    fields = ['name','file','video']
    template_name = 'teacher_dashboard/update.html'
    success_url = '/dashboard/teacher_groups/'