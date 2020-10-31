# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# def students_list(request):
#     temlate = loader.get_template('demo.html')
#     context = RequestContext(request, {})
#     return HttpResponse(temlate.reder(context))
def students_list(request):
    return render(request, 'students/students_list.html',{})
    # return HttpResponse('<h1>Hello World</h1>')
# Create your views here.

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' %sid)



def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)

# Views for Grops

def groups_list(request):
    return HttpResponse('<h1>Groups List</h1>')

def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1> Delete Group %s</h1>' % gid)