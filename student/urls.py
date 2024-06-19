from django.urls import path
from student.views import fetch_student, list_student, create_class

urlpatterns = [
    path('',fetch_student,name="fetch-student"),
    path('list',list_student,name="list-student"),
    path('class/create', create_class, name='create_class')
]