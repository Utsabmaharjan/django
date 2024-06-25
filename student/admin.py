from django.contrib import admin
from student.models import BroadwayStudent, StudentClass

# Register your models here.

@admin.register(BroadwayStudent)
class BroadwayStudentAdmin(admin.ModelAdmin):
    list_display=['id','name','address','phone']
    search_fields=['name','address']

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'section', 'status', 'class_type', 'class_link']