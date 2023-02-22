from django.shortcuts import render,redirect
from eduspace.decorators import studentonly
from teaching.models import Group
from user.models import Student
# Create your views here.

@studentonly
def my_lesson(request,group_number = None):
    if request.user.is_staff:
        groups = Group.objects.all()
    else:
        student = Student.objects.get(user = request.user)
        groups = student.group_set.all()
    if groups.exists():
        if group_number:
            try:
                group = groups.get(id = group_number)
            except:
                return redirect('404')
        else:
            group = groups[0]
    context = {
        'groups':groups,
        'group':group
    }
    return render(request,'main/library.html',context=context)