# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from ..models import Resoult
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from  ..util import paginate
from ..helpers.login_premissions import LoginRequiredClass, PremissionRequiredClass

# Views for Exams

def resoult_list(request):
    resoult = Resoult.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'student', 'exam', 'teacher'):
        resoult = resoult.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            resoult = resoult.reverse()

    # set nomber on page

    # ================OLD pagination======================
    # number_on_page = request.GET.get('number_on_page')
    # if number_on_page < 1:
    #     number_on_page = 1
    #
    # loading_step = 1
    #
    # # paginate students
    # paginator = Pagination(resoult, number_on_page, loading_step)
    # # paginator = Paginator(students, 3)
    # page = request.GET.get('page')
    # try:
    #     resoult = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     resoult = paginator.page(1)
    #
    # except EmptyPage:
    #     # If page is out of range (e.g 9999), deliver last page of resoult
    #     resoult = paginator.page(paginator.num_pages)

    # ================OLD pagination end======================

    context1 = {}
    # context1['1'] ='1'

    context = paginate(resoult, 3, request, context1, var_name='')

    return render(request,'students/exams_resoult.html',
                  {'resoult':context})


# def exams_add(request):
#     return HttpResponse('<h1>s Add Form</h1>')
#
# def groups_edit(request, gid):
#     return HttpResponse('<h1>Edit Groups %s</h1>' %gid)
#
# def groups_delete(request, gid):
#     return HttpResponse('<h1> Delete Group %s</h1>' %gid)