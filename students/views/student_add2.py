# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from ..models import Student
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


class AddStudentsForm(ModelForm):
    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        super(AddStudentsForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_add2')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set field propertyes
        self.helper.help_tex_iline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.form_show_labels = True

        # add button
        self.helper.add_input(Submit('add_button', u'Сохранить', css_class="btn btn-primary"))
        self.helper.add_input(Submit('cancel_button', u'Отменить', css_class="btn-link"))
        # self.helper.layout[-1] = FormActions(
        #     Submit('add_button', u'Сохранить', css_class="btn btn-primary"),
        #     Submit('cancel_button', u'Отменить', css_class="btn-link"),
        # )


class AddStudents(CreateView):
    model = Student
    template_name = 'students/students_add2.html'
    form_class = AddStudentsForm

    def get_success_url(self):
        return u'%s?status_message=Студент успешно добавлен!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Добавление отменено!' % reverse('home'))
        else:
            return super(AddStudents, self).post(request, *args, **kwargs)
