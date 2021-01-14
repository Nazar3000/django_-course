# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Teacher, Student, Group, Exam, Resoult, MonthJournal
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError



class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        ''' Check if student is leader in any group.
        If yes, then ensure it's the same as selected group.'''
        # get group where current student is a leader

        groups = Group.objects.filter(leader=self.instance)
        grop_name = Group.objects.get(leader=self.instance)
        leader = self.cleaned_data['student_group']
        if len(groups) > 0 and \
                leader != groups[0]:
            raise ValidationError(u'Этот студент является старостой другой группы:%s' % grop_name, code='invalid')

        return self.cleaned_data['student_group']



class GroupFormAdmin(ModelForm):

    def clean_leader(self):
        ''' Check if student is leader in any group.
                If yes, then ensure it's the same as selected group.'''
        # get group where current student is a leader
        # raise ValidationError(u'Этот студент является старостой другой группы!!!', code='invalid')
        students = Student.objects.filter(student_group=self.instance)
        leader = self.cleaned_data['leader']

        if leader is not None:
            for student in students:
                if leader == student:
                    return self.cleaned_data['leader']
                else:
                    raise ValidationError(u'Этот студент состоит в другой группе: %s' % leader.student_group,
                                          code='invalid')




class StudentAdmin(admin.ModelAdmin):

    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group', 'ticket']
    list_per_page = 20
    search_fields = ['last_name', 'first_name', 'ticket', 'student_group']
    form = StudentFormAdmin
    actions = ['copy_students']

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk':obj.id})

    def copy_students(self, request, queryset):
        queryset = queryset.filter()

        queryset.pk = None
        for obj in queryset:
            obj.pk = None
            obj.save()



# @admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupFormAdmin
    list_display = ['title', 'leader', 'notes']
    list_display_links = ['title']
    list_editable = ['leader']
    list_per_page = 10
    search_fields = ['title', 'leader', 'notes']




# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam)
admin.site.register(Resoult)
admin.site.register(Teacher)
admin.site.register(MonthJournal)

