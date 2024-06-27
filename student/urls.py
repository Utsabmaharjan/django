from django.urls import path
from student.views import (
    fetch_student,
    list_class,
    create_class,
    edit_class,
    delete_class,
    StudentClassView
)
urlpatterns = [
    path('',fetch_student,name="fetch-student"),
    path('class',list_class,name="list-class"),
    path('class/create',create_class,name="create_class"),
    path('class/edit/<id>',edit_class,name="edit_class"),
    path('class/delete/<id>',delete_class,name="delete_class"),

    # class based view
    path('classed/class',StudentClassView.as_view(),name="classed-view-list")

    
]
