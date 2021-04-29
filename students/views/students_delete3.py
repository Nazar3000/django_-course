# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from ..models import Student

def students_delete(request, pk):
    if request.POST.get('delete_button') is not None:
        studentobj = Student.objects.get(pk=pk)

        studentobj.delete()

        messages.add_message(request, messages.ERROR,
                             'Студент %s успешно удален!' % studentobj)
        return HttpResponseRedirect('%s?status_message=Студент %s успешно удален!' % (
            reverse('home'), studentobj))


    elif request.POST.get('cancel_button') is not None:
        # redirect to home page on cancel button
        messages.add_message(request, messages.ERROR,
                             'Удаление студента %s отменено!' % request.POST.get('first_name', '').strip())
        return HttpResponseRedirect('%s?status_message=Изменение студента %s отменено!' % (
        reverse('home'), request.POST.get('first_name', '').strip()))
    else:
        student = Student.objects.get(pk=pk)
        return render(request, 'students/students_confirm_delete3.html',
                      {'student': student })