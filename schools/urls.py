from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('register/',views.register,name='register'),
    path('subs/',views.submit,name='subs'),
    # path('name/',views.contact,name='name')
    path('fee/',views.fee,name='fee'),
    # Schools List
    path('schools_list/',views.schools_list,name='schools_list'),
    # Buy
    path('buy/',views.buy,name='buy'),
    path('contact/',views.contact,name='contact'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('students/',views.students,name='students'),
    path('students/<int:roll>profile/',views.profile,name='profile'),
    path('teachers/',views.teachers,name='teachers'),
    path('teachers/<int:number>/',views.profileteacher,name='profileteacher'),
    # School
    path('<slug:school_name>/',views.school_home,name='schools_home'),
    
    # Teacher
    path('teacher/<int:teacher_id1>t/',views.teacher_home,name='teacher_home'),
    path('teacher/<int:teacher_id1>/<int:class1>th/',views.teacher_class,name='teacher_class'),
    path('students/<int:stu_roll_no>s/',views.student_home,name='student_home'),
    
    
]+[path('accounts/',include('django.contrib.auth.urls')),]