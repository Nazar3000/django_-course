# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from ..models import Group, Student
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView, UpdateView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.forms import ModelForm, ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from ..util import paginate

# Views for Grops vs old pagination

# def groups_list(request):
#     groups = Group.objects.all()
#
#     # try to order groups list
#     order_by = request.GET.get('order_by', '')
#     if order_by in ('title', 'leader'):
#         groups = groups.order_by(order_by)
#         if request.GET.get('reverse', '') == '1':
#             groups = groups.reverse()
#
#     # set nomber on page
#
#     number_on_page = request.GET.get('number_on_page')
#     if number_on_page < 1:
#         number_on_page = 1
#
#     loading_step = 2
#
#     # paginate students
#     paginator = Pagination(groups, number_on_page, loading_step)
#     # paginator = Paginator(students, 3)
#     page = request.GET.get('page')
#     try:
#         groups = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         groups = paginator.page(1)
#
#     except EmptyPage:
#         # If page is out of range (e.g 9999), deliver last page of resoult
#         groups = paginator.page(paginator.num_pages)
#
#     return render(request, 'students/groups_list.html',
#                   {'groups': groups})

def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    context1 = {}
    # context1['1'] ='1'

    context = paginate(groups, 3, request, context1, var_name='groups')

    # return context
    return render(request, 'students/groups_list.html',
                  {'groups': context})





# def groups_edit(request, gid):
#     return HttpResponse('<h1>Edit Groups %s</h1>' % gid)


class GroupUpdateForm(ModelForm):

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
                    raise ValidationError(u'Этот студент состоит в другой группе: %s'%leader.student_group, code='invalid')

    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('groups_edit', kwargs={'pk': kwargs['instance'].id})
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



class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/group_update_form.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Группа успешно отредактирована!'\
    % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редактирование группы отменено!'
                                        % reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupsDeleteView(DeleteView):
    # error_url = reverse('groups_delete')
    # group_id = object
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        # group_id = request.POST.get(object)

        self.object = self.get_object()
        # self.object = get_queryset()
        object = self.object
        group_id = object.id
        related_stud = len(Student.objects.filter(student_group=group_id))
        students_ns = related_stud

        # success_url = self.get_success_url()

        try:
            # self.object.delete()
            # return HttpResponseRedirect(success_url)
            self.object.delete()
            messages.add_message(request, messages.ERROR,
                                 u'Группа %s успешно удалена!' % object)
            # return HttpResponseRedirect(success_url)
            return HttpResponseRedirect(u'%s?status_message=Группа %s успешно удалена!' % (reverse('home'), object))
        except:

            messages.add_message(request, messages.ERROR,
                                 u'Эта группа все еще содержит %s студентов и не может быть удалена' % students_ns)
            return render(request, 'students/groups_confirm_delete.html', {'object': object})


    # def get_success_url(self):
    #     messages.add_message(request, messages.ERROR,
    #                          u'Группа %s успешно удалена!' % object)
    #
    #     return u'%s?status_message=Группа %s успешно удалена!' % (reverse('home'), object)

    # def get_error_url(self):
    #     return u'%s?status_message=Группа не удалена так как в ней есть студенты!' % reverse('home')
    # def get_error_url(self):
    #     # if self.error_url:
    #     return self.error_url.format(**self.object.__dict__)
    # else:
    #     raise ImproperlyConfigured(
    #         "No error URL to redirect to. Provide a error_url.")

# def groups_delete(request, gid):
#     return HttpResponse('<h1> Delete Group %s</h1>' %gid)

class GroupsAddForm(ModelForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupsAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('groups_add')
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

class AddGroup(CreateView):
    model = Group
    template_name = 'students/group_update_form.html'
    form_class = GroupsAddForm

    def get_success_url(self):
        return u'%s?status_message=Группа успешно добавлена!' \
               % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Добавление группы отменено!'
                                        % reverse('groups'))
        else:
            return super(AddGroup, self).post(request, *args, **kwargs)