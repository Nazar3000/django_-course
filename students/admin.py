from django.contrib import admin
from .models import Student, Group, Exam, Teacher, Resoult
from django.core.urlresolvers import reverse

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group', 'ticket']
    list_per_page = 20
    search_fields = ['last_name', 'first_name', 'ticket', 'student_group']
    actions = ['copy_students']
    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk':obj.id})

    def copy_students(self, request, queryset):
        queryset = queryset.filter()

        queryset.pk = None
        for obj in queryset:
            obj.pk = None
            obj.save()




class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'notes']
    list_display_links = ['title']
    list_editable = ['leader']
    list_per_page = 10
    search_fields = ['title', 'leader', 'notes']

    # def view_on_sitr(self, obj):
    #
    #     return reverse('students_edit', kwargs={'pk':obj.id})
    #

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam)
admin.site.register(Teacher)
admin.site.register(Resoult)

