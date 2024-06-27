from django import forms
from student.models import StudentClass

class StudentClassForm(forms.ModelForm):
    started_at = forms.DateField(widget=forms.DateInput())
    class Meta:
        model = StudentClass
        # fields ='__all__'
        exclude =['created_at']
        # fields = ['name','ended_at']
