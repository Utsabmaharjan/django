from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from student.models import BroadwayStudent, StudentClass
from django.http import HttpResponse
from student.forms import StudentClassForm


# Create your views here.
# function based views


def fetch_student(request):
    a = BroadwayStudent.objects.all()
    context = {"data": a}
    return render(request, "student/index.html", context)


def list_student(request):
    return HttpResponse("this is another view for testing")


def list_class(request):
    context = {"data": StudentClass.objects.all()}
    return render(request, "class/index.html", context)


def create_class(request):
    form = StudentClassForm()
    if request.method=='POST':
        form = StudentClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/class')
        else:
            print(form.errors)

    context = {"data": "this is create class form", "form": form}
    return render(request, "class/create.html", context)

def edit_class(request,id):
    student_class = StudentClass.objects.get(id=id)
    form = StudentClassForm(instance=student_class)
    if request.method=='POST':
        form = StudentClassForm(request.POST ,request.FILES or None, instance=student_class)
        if form.is_valid():
            form.save()
            return redirect('/student/class')
        else:
            print(form.errors)

    context ={
        "data":student_class,
        "form":form
    }
    return render(request,'class/edit.html',context)

def delete_class(request, id):
    student_class = StudentClass.objects.get(id=id).delete()
    return redirect('/student/class')


class StudentClassView(ListView):
    model = StudentClass
    template_name = 'class/index.html'
    context_object_name ='data'

    def get_queryset(self):
        return self.model.objects.filter(status=False)
    