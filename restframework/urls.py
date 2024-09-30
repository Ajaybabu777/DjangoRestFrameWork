from django.urls import path
from .views import *
from restframework import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('student_post/',views.student_post,name="student_post"),
    path('student_put/<id>/',views.student_put,name = "student_put"),
    path('delete_student/<id>/',views.delete_student,name = "delete_student"),
    path('register_user/',views.register_user,name = "register_user")
]