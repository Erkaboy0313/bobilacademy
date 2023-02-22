from math import fabs
from django.db.models import Manager

class ProjectManager(Manager):

    def tottal_projects(self):
        return self.all().count()

class StudentManager(Manager):
    
    def tottal_students(self):
        return self.all().count()

class TeacherManager(Manager):

    def tottal_teachers(self):
        return self.all().count()

class PaymentManager(Manager):
    
    def tottal_payment(self):
        return sum(list(self.values_list('amount',flat=True)))

class CourseManager(Manager):
    
    def tottal_courses(self):
        return self.all().count()
