from django.contrib import admin
from student.models import BroadwayStudent, StudentClass

# Register your models here.
# admin.site.register(BroadwayStudent)


@admin.register(BroadwayStudent) #wrapper function@
class BroadwayStudentAdmin(admin.ModelAdmin):
    list_display = ["id", "student_class", "name", "address", "phone"]
    search_fields = ["name", "address"]


@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "section", "status", "class_type", "class_link","created_at"]

# class StudentClassAdmin(admin.ModelAdmin):
#     def get_readonly_fields(self, request, obj=None):
#         if obj:  # This means the object already exists (it's not a new object)
#             return [field.name for field in obj._meta.fields]
#         else:
#             return []

#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         self.readonly_fields = self.get_readonly_fields(request, obj=self.get_object(request, object_id))
#         return super().change_view(request, object_id, form_url, extra_context)

#     def add_view(self, request, form_url='', extra_context=None):
#         self.readonly_fields = self.get_readonly_fields(request)
#         return super().add_view(request, form_url, extra_context)

# admin.site.register(StudentClass, StudentClassAdmin)
