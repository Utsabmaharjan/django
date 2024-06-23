from django.shortcuts import render
from student.models import BroadwayStudent, StudentClass
from django.http import HttpResponse
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
       form = StudentClass
        
       context = {
             "form": "this is create class form"
        }
       
       return render(request, 'class/create.html', context)
   