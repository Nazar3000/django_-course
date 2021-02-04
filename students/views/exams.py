# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Exam
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from  ..util import paginate, get_current_group
from django.views.generic import UpdateView, CreateView, DeleteView
from  django.forms import ModelForm
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions


# Views for Exams

def exams_list(request):
    # check if we need to show only one group exams
    current_group = get_current_group(request)
    if current_group:
        exams = Exam.objects.filter(exams_group=current_group)
    else:
        # otherwiese show all exams
        exams = Exam.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'date', 'student_group', 'teacher'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # set nomber on page


# ================OLD pagination======================
#     number_on_page = request.GET.get('number_on_page')
#     if number_on_page < 1:
#         number_on_page = 1
#
#     loading_step = 1
#
#     # paginate students
#     paginator = Pagination(exams, number_on_page, loading_step)
#     # paginator = Paginator(students, 3)
#     page = request.GET.get('page')
#     try:
#         exams = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         exams = paginator.page(1)
#
#     except EmptyPage:
#         # If page is out of range (e.g 9999), deliver last page of resoult
#         exams = paginator.page(paginator.num_pages)

    # ================OLD pagination end======================
    context1 = {}
    # context1['1'] ='1'

    context = paginate(exams, 3, request, context1, var_name='exams')
# ==================New pagination========================

    return render(request,'students/exams.html',
                  {'exams':context})


# def exams_add(request):
#     return HttpResponse('<h1>s Add Form</h1>')
#
# def groups_edit(request, gid):
#     return HttpResponse('<h1>Edit Groups %s</h1>' %gid)
#
# def groups_delete(request, gid):
#     return HttpResponse('<h1> Delete Group %s</h1>' %gid)

class ExamsUpdateForm(ModelForm):

    class Meta:
        model = Exam

    def __init__(self, *args, **kwargs):
        super(ExamsUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('exams_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set field propertyes
        self.helper.help_tex_iline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.layout = Layout(
            '',
            'title',

            CustomBirthdayField('date'),

            'exams_group',
            'teacher',
            'notes',
        )

        # add button
        self.helper.add_input(Submit('add_button', u'Сохранить', css_class="btn btn-primary"))
        self.helper.add_input(Submit('cancel_button', u'Отменить', css_class="btn-link"))
        # self.helper.layout[-1] = FormActions(
        #     Submit('add_button', u'Сохранить',css_class="btn btn-primary" ),
        #     Submit('cancel_button', u'Отменить', css_class="btn-link"),
        # )


class ExamsCreateForm(ModelForm):

    class Meta:
        model = Exam

    def __init__(self, *args, **kwargs):
        super(ExamsCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('exam_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set field propertyes
        self.helper.help_tex_iline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.layout = Layout(
            '',
            'title',

            CustomBirthdayField('date'),

            'exams_group',
            'teacher',
            'notes',
        )

        # add button
        self.helper.add_input(Submit('add_button', u'Сохранить', css_class="btn btn-primary"))
        self.helper.add_input(Submit('cancel_button', u'Отменить', css_class="btn-link"))
        # self.helper.layout[-1] = FormActions(
        #     Submit('add_button', u'Сохранить',css_class="btn btn-primary" ),
        #     Submit('cancel_button', u'Отменить', css_class="btn-link"),
        # )


class CustomBirthdayField(Field):
    template = 'students/date_field.html'

class ExamsUpdateView(UpdateView):
    model = Exam
    template_name = 'students/exams_form.html'
    form_class = ExamsUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Экзамен успешно отредактирован!'\
    % reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редактирование экзамена отменено!'
                                        % reverse('exams'))
        else:
            return super(ExamsUpdateView, self).post(request, *args, **kwargs)



class AddExam(CreateView):
    model = Exam
    template_name = 'students/exams_form.html'
    form_class = ExamsCreateForm

    def get_success_url(self):
        return u'%s?status_message=Экзамен успешно бдобавлен!'\
    % reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Добавлнеие экзамена отменено!'
                                        % reverse('exams'))
        else:
            return super(AddExam, self).post(request, *args, **kwargs)


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'students/exam_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        # group_id = request.POST.get(object)

        self.object = self.get_object()
        # self.object = get_queryset()
        object = self.object
        group_id = object.id
        # related_stud = len(Student.objects.filter(student_group=group_id))
        # students_ns = related_stud

        # success_url = self.get_success_url()

        try:
            # self.object.delete()
            # return HttpResponseRedirect(success_url)
            self.object.delete()
            messages.add_message(request, messages.ERROR,
                                 u'"Экзамен" %s успешно удален!' % object)
            # return HttpResponseRedirect(success_url)
            return HttpResponseRedirect(u'%s?status_message=Экзамен %s успешно удален!' % (reverse('exams'), object))
        except:

            messages.add_message(request, messages.ERROR,
                                 u'Произошла какая-то хуйня при удалении этого экзамена %s посмотри поля в модели эзамена' % object)
            return render(request, 'students/exam_confirm_delete.html', {'object': object})