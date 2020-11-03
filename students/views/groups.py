# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# Views for Grops

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'MtM-21',
         'leader': {'id':1, 'name': u'Андрей Корост'}},
        {'id':2,
         'name': u'MtM-22',
         'leader':{'id':2, 'name':u'Назар Мазур'}},
        {'id': 3,
         'name': 'MtM-23',
         'leader': {'id':3, 'name':u'Виталий Подоба'}},
    )
    return render(request,'students/groups_list.html',
                  {'groups':groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1> Delete Group %s</h1>' % gid)