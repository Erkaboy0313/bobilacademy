from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('not_found',error,name='404'),
    path('courses/',courses,name='courses'),
    path('contacts/',contacts,name='contacts'),
    path('about/',about,name='about'),
    path('course/<int:id>',course_type,name='course_type'),
    path('login/',log_in,name='login'),
    path('register/course/',register_course,name='register_course'),



    #admin part urls
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/course/',course,name='course'),
    path('dashboard/sugessions/',sugessions,name='sugessions'),
    path('dashboard/modul/',modul,name='modul'),
    path('dashboard/news/',news,name='news'),
    path('dashboard/payment_history/',payment_history,name='payment_history'),
    path('dashboard/payment/',payment,name='payment'),
    path('dashboard/statistics/',statistics,name='statistics'),
    path('dashboard/student/',student,name='student'),
    path('dashboard/teacher/',teacher,name='teacher'),
    path('dashboard/register/',register,name='register'),
    path('dashboard/group/',group,name='group'),
    path('dashboard/teacher_groups/',teacher_group,name='my_groups'),
    path('dashboard/admins/',addAdmin,name='admins'),

    #updating part of admin

    path('dashboard/course/update/<int:pk>/',CourseUpdateView.as_view(),name='update_course'),
    path('dashboard/module/update/<int:pk>/',ModuleUpdateView.as_view(),name='update_modul'),
    path('dashboard/Student/update/<int:pk>/',StudentUpdateView.as_view(),name='update_student'),
    path('dashboard/Teacher/update/<int:pk>/',TeacherUpdateView.as_view(),name='update_teacher'),
    path('dashboard/Admin/update/<int:pk>/',AdminUpdateView.as_view(),name='update_admin'),
    path('dashboard/News/update/<int:pk>/',NewsUpdateView.as_view(),name='update_news'),
    path('dashboard/Group/update/<int:pk>/',GroupUpdateView.as_view(),name='update_group'),
    path('dashboard/teacher_modul/update/<int:pk>/',GroupModulUpdateView.as_view(),name='update_teacher_modul'),
    path('dashboard/teacher_theme/update/<int:pk>/',GroupThemeUpdateView.as_view(),name='update_teacher_theme'),

    #deleting part of admin

    path('dashboard/remove_course/',removecourse,name='removecourse'),
    path('dashboard/remove_modul/',removemodule,name='removemodule'),
    path('dashboard/remove_student/',removeuser,name='removestudent'),
    path('dashboard/remove_news/',removenews,name='removenews'),
    path('dashboard/remove_register/',reomoveRegister,name='removeRegister'),
    path('dashboard/remove_group/',reomoveGroup,name='removeGroup'),
    path('dashboard/remove_admin/',removeadmin,name='removeGroup'),


    #blocking

    path('dashboard/blockuser/',block_student,name='blockuser'),
    path('dashboard/status/',change_status,name='status'),
    path('dashboard/sugession_status/',sugession_status,name='sugession_status'),

]