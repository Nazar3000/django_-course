# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from ..models import Student
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class AddStudents(CreateView):
    model = Student
    template_name = 'students/students_add2.html'


    def get_success_url(self):
        return u'%s?status_message=Студент успешно добавлен!'% reverse('students_add2')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Добавление отменено!'% reverse('home'))
        else:
            return super(AddStudents, self).post(request, *args, **kwargs)