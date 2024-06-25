from django.urls import path
from student.views import fetch_student, featch_class, create_class, edit_class, delete_class, create_student_class, edit_student_class, delete_student_class, StudentClassView
urlpatterns = [
        path('', fetch_student, name="fetch-student"),
        path('class', featch_class, name="class-list"),
        path('class/form', create_class, name='create-list'),
        path('class/edit/<id>', edit_class, name='edit-class'),
        path('class/delete/<id>', delete_class, name='delete-class'),
        path('create', create_student_class, name="create-student-list"),
        path('edit/<id>', edit_student_class, name="edit-student-list"),
        path('delete/<id>', delete_student_class, name="delete-student-list"),

        path('classed/class', StudentClassView.as_view(), name="student_class_view")


]

