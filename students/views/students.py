# -*- coding: utf-8 -*-

from django.template.defaultfilters import filesizeformat
# from __future__ import unicode_literals
from django.conf import settings
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse


# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from ..models import Student, Group


# Views for Students

def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by','')
    if order_by in ('last_name', 'first_name', 'ticket', 'student_group'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # set nomber on page

    number_on_page= request.GET.get('number_on_page')
    if number_on_page <1:
        number_on_page=1

    loading_step = 1


    # paginate students
    paginator = Pagination(students, number_on_page, loading_step)
    # paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g 9999), deliver last page of resoult
        students = paginator.page(paginator.num_pages)
    return render(request, 'students/students_list.html',
                  {'students': students})


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



def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)

