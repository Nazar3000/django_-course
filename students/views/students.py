# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import time
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

def students_add(request):

    # was from postes?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors={}

            # validate students data will go here
            # data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}
            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Имя есть обязательным"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия тоже есть обязательной"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата рождения есть обязательной"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday']=u"Введите корректный формат даты (напр.1984-12-30)"


                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета есть обязательным"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) !=1:
                    errors['student_group'] = u"Выберите коректную группу"

                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            # save studen
            if not errors:
                student = Student(**data)
                student.save()

                # redirect to students list
                return  HttpResponseRedirect(reverse('home'))
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups':Group.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))
    else:
         # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})
    # Если форма небыла запощена:
    #     возвращаем код начального состояния формы



def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' %sid)



def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' %sid)

