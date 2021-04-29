# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from ..models import Student, Group
from django import forms


class edit_form(forms.Form):
    # name=Group.objects.all()
    first_name = forms.CharField(
        max_length=256,
        # initial=name,
        label="Имя")

    last_name = forms.CharField(
        label="Фамилия",
        max_length=256)

    middle_name = forms.CharField(
        label="Отчество",
        max_length=256)

    birthday = forms.DateField(
        label="Дата рождения")

    photo = forms.ImageField(
        label="Фото")

    ticket = forms.CharField(
        label="Билет",
        max_length=256)

    # notes = forms.TextField(
    #     label=u"Дополнительные заметки",
    #     )

class Students_edit(FormView):

    template_name = 'students/students_edit2.html'
    form_class = edit_form
    success_url = '/'


    def form_valid(self, form):
        """This
                method is called
                for valid data"""
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birthday = form.cleaned_data['birthday']
        ticket = form.cleaned_data['ticket']
        student_group = form.cleaned_data['student_group']
        photo = form.cleaned_data['photo']



        student = Student(first_name, last_name, birthday, ticket, student_group, photo)
        student.save()
        return super(Students_edit, self).form_valid(form)