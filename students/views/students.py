# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name':u'Андрей',
         'last_name': u'Корост',
         'ticket': 235,
         'image': 'img/download.jpeg'},
        {'id': 2,
         'first_name': 'Назар',
         'last_name': u'Мазур',
         'ticket': 137,
         'image': 'img/download (1).jpeg'
        },
        {'id': 3,
         'first_name': 'Виталий',
         'last_name': u'Подоба',
         'ticket': 39,
         'image': 'img/download (2).jpeg'
         }
    )
    return render(request, 'students/students_list.html',
                  {'students':students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' %sid)



def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)

