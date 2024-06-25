from django.db import models


# Create your models here.

class StudentClass(models.Model):
    name = models.CharField(verbose_name="Class name", max_length=30, blank=False, null=True)
    section = models.CharField(verbose_name="class Section", max_length=40)
    image = models.ImageField(upload_to='studentclass/', null=True, blank=True)
    status =  models.BooleanField(default=False)
    class_type = models.CharField(verbose_name="class type", max_length=10, null=True, blank=True)
    class_link = models.URLField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    started_at =  models.DateField(null=True, blank=True)
    ended_at = models.DateField(name="ended", null=True, blank=True)
    
    def __str__(self):
        return self.name

class BroadwayStudent(models.Model):
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255, null=True,help_text='student name')
    address = models.CharField(max_length=33, null=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    
    def _str_(self):
        return self.name