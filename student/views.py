from django.shortcuts import render, redirect
from student.models import BroadwayStudent, StudentClass
from student.forms import StudentClassForm, StudentForm
from django.views.generic.list import ListView
# Create your views here.

def fetch_student(request):
        a=BroadwayStudent.objects.all()
       
        #return HttpResponse(a)
        context = {
                "data":a
        }
        return render(request, 'student/index.html', context)


def featch_class(request):
        b=StudentClass.objects.all()
       
        #return HttpResponse(a)
        context = {
                "data":b
        }
        return render(request, 'class/index.html', context)

def create_class(request):
       form = StudentClassForm
       if request.method=='POST':
               form= StudentClassForm(request.POST)
               if form.is_valid():
                       form.save()
                       return redirect('/student/class')
               else:
                       print(form.errors)


       context = {
        "form": form
        }
       
       return render(request, 'class/create.html', context)

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
      Student_class = StudentClass.objects.get(id=id).delete()
      return redirect('/student/class')

def create_student_class(request):
       form = StudentForm
       if request.method=='POST':
               form= StudentForm(request.POST)
               if form.is_valid():
                       form.save()
                       return redirect('/student')
               else:
                       print(form.errors)


       context = {
        "form": form
        }
       
       return render(request, 'student/create.html', context)

def edit_student_class(request,id):
    student = BroadwayStudent.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method=='POST':
        form = StudentForm(request.POST ,request.FILES or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/student')
        else:
            print(form.errors)

    context ={
        "data":student,
        "form":form
    }
    return render(request,'student/edit.html',context)

def delete_student_class(request, id):
      student = BroadwayStudent.objects.get(id=id).delete()
      return redirect('/student')

class StudentClassView(ListView):
      model = StudentClass
      template_name = 'class/index.html'
      context_object_name = 'data'