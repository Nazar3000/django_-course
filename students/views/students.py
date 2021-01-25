# -*- coding: utf-8 -*-

from django.template.defaultfilters import filesizeformat
# from __future__ import unicode_literals
from django.conf import settings
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DeleteView
from django.forms import ModelForm, ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from ..util import paginate



# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from ..models import Student, Group

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student

    def clean_student_group(self):
        ''' Check if student is leader in any group.
        If yes, then ensure it's the same as selected group.'''
        # get group where current student is a leader



        groups = Group.objects.filter(leader=self.instance)
        grop_name = Group.objects.get(leader=self.instance)
        leader = self.cleaned_data['student_group']
        if len(groups) > 0 and \
            leader != groups[0]:
            raise ValidationError(u'Этот студент является старостой другой группы:%s'%grop_name, code='invalid')

        return self.cleaned_data['student_group']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit', kwargs={'pk':kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set field propertyes
        self.helper.help_tex_iline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add button
        self.helper.add_input(Submit('add_button', u'Сохранить', css_class="btn btn-primary"))
        self.helper.add_input(Submit('cancel_button', u'Отменить', css_class="btn-link"))
        # self.helper.layout[-1] = FormActions(
        #     Submit('add_button', u'Сохранить',css_class="btn btn-primary" ),
        #     Submit('cancel_button', u'Отменить', css_class="btn-link"),
        # )

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_form.html'
    form_class = StudentUpdateForm


    def get_success_url(self):
        return u'%s?status_message=Студент успешно добавлен!' \
               % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редактирование студента отменено!'
                                        % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)




# Views for Students

def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by','')
    if order_by in ('last_name', 'first_name', 'ticket', 'student_group'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

# ===============Old pagination===================

    # set nomber on page
    #
    # number_on_page= request.GET.get('number_on_page')
    # if number_on_page <1:
    #     number_on_page=1
    #
    # loading_step = 1
    #
    #
    # # paginate students
    # paginator = Pagination(students, number_on_page, loading_step)
    # # paginator = Paginator(students, 3)
    # page = request.GET.get('page')
    # try:
    #     students = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     students = paginator.page(1)

    # except EmptyPage:
        # If page is out of range (e.g 9999), deliver last page of resoult

        # students = paginator.page(paginator.num_pages)

    # ===============Old pagination END===================
    context1 = {}
    context = paginate(students, 4, request, context1, var_name='student')
    return render(request, 'students/students_list.html',
                  {'students': context})


    # students = (
    #     {'id': 1,
    #      'first_name':u'Андрей',
    #      'last_name': u'Корост',
    #      'ticket': 235,
    #      'image': 'img/download.jpeg'},
    #     {'id': 2,
    #      'first_name': 'Назар',
    #      'last_name': u'Мазур',
    #      'ticket': 137,
    #      'image': 'img/download (1).jpeg'
    #     },
    #     {'id': 3,
    #      'first_name': 'Виталий',
    #      'last_name': u'Подоба',
    #      'ticket': 39,
    #      'image': 'img/download (2).jpeg'
    #      }
    # )
    # return render(request, 'students/students_list.html',
    #               {'students':students})



def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' %sid)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Студент успешно удален!' % reverse('home')

# def students_delete(request, sid):
#     return HttpResponse('<h1>Delete Student %s</h1>' %sid)

