# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from ..models import Group, Student
from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse
from django.contrib import messages


# Views for Grops

def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # set nomber on page

    number_on_page = request.GET.get('number_on_page')
    if number_on_page < 1:
        number_on_page = 1

    loading_step = 1

    # paginate students
    paginator = Pagination(groups, number_on_page, loading_step)
    # paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)

    except EmptyPage:
        # If page is out of range (e.g 9999), deliver last page of resoult
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html',
                  {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups %s</h1>' % gid)


class GroupsDeleteView(DeleteView, SingleObjectMixin):
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

        success_url = self.get_success_url()

        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except:

            messages.add_message(request, messages.ERROR,
                                 u'Эта группа все еще содержит %s студентов и не может быть удалена' % students_ns)
            return render(request, 'students/groups_confirm_delete.html', {'object': object})


    def get_success_url(self):

        return u'%s?status_message=Группа успешно удалена!' % reverse('home')

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
