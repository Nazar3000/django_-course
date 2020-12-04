from django.contrib import admin
from .models import Student, Group, Exam, Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Teacher)
