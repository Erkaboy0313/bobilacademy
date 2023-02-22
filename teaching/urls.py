from django.urls import path
from .views import *

urlpatterns = [
    path('mycourse/',my_lesson,name='mycourses'),
    path('mycourse/<int:group_number>/',my_lesson,name='mycourses')
]