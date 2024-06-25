from django import forms
from student.models import StudentClass, BroadwayStudent

class StudentClassForm(forms.ModelForm):

    
    class Meta:
        model = StudentClass
        fields = '__all__'

class StudentForm(forms.ModelForm):

    
    class Meta:
        model = BroadwayStudent
        fields = '__all__'