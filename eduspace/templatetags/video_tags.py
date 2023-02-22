from django import template
from user.models import Student, Teacher
from teaching.models import Payment
from datetime import datetime

register = template.Library()


@register.simple_tag
def groups(Teacher):
    return Teacher.group_set.all().count()

@register.simple_tag
def students(Teacher):
    students = []
    for g in Teacher.group_set.all():
        students.append(g.students.all().count())
    return sum(students)

@register.simple_tag
def payment_status(student,group):
    this_month = datetime.now().month
    this_year = datetime.now().year
    date = datetime.strptime(f'1 {this_month} {this_year}','%d %m %Y')
    last_payments = student.payment_set.filter(time__gte = date , group = group).values_list('amount', flat = True)
    return sum(last_payments) - group.cost