# -*- coding: utf-8 -*-
import os
from django.template.defaultfilters import filesizeformat
from django.conf import settings
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext,
from django.core.urlresolvers import reverse
from ..models import Student, Group
from PIL import Image


def students_edit3(request, pk):


    # was form posted?
    if request.method == "POST":
        student = Student.objects.get(pk=pk)
        # studentobj = Student.objects.filter(id=pk)
        # studentobj = student
        group = student.student_group




        # was from edit button cliked?
        if request.POST.get('edit_button') is not None:
            studentobj = Student.objects.get(pk=pk)
            # errors collection
            errors={}

            # validate students data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                                'notes': request.POST.get('notes')}
            studentobj.middle_name= data['middle_name']
            studentobj.notes = data['notes']


            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Имя есть обязательным"
                errors['frist_name_id'] = "Имя"
            else:
                data['first_name'] = first_name
                studentobj.first_name = data['first_name']
            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия тоже есть обязательной"
                errors['last_name_id'] = "Фамилия"
            else:
                data['last_name'] = last_name
                studentobj.last_name = data['last_name']

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата рождения есть обязательной"
                errors['birthday_id'] = "Дата"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Вы ввели %s Введите корректный формат даты (напр.1984-12-30)" % (birthday)
                    errors['birthday_id'] = "Дата"

                else:
                    data['birthday'] = birthday
                    studentobj.birthday = data['birthday']
            # data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета есть обязательным"
                errors['ticket_id'] = "Билет"
            else:
                data['ticket'] = ticket
                studentobj.ticket = data['ticket']

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу для студента"
                errors['student_group_id'] = "Группа"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Выберите коректную группу"
                    errors['student_group_id'] = "Группа"

                else:
                    data['student_group'] = groups[0]
                    studentobj.student_group = data['student_group']

            # Валидация фото без Pillow
            photo = request.FILES.get('photo')

            if photo:

                validate_type = validate_file_extension(photo)
                data_type = type(photo)
                if validate_type is True:
                    validate = validate_size(photo)
                    if validate is True:
                        data['photo'] = photo
                        studentobj.photo = data['photo']
                    else:
                        errors['photo'] = u"Фото должно быть не больше 2 мб и не меньше 1 кб"
                        errors['photo_id'] = "Фото"

                else:
                    errors['photo'] = u"Это не фото, ты ошибся"
                    errors['photo_id'] = "Фото"

            if not errors:
                # studentobj = Student.objects.get(pk=pk)
                # student = Student(**data)
                # studentobj.first_name = data['first_name']
                # studentobj.last_name = data['last_name']
                # studentobj.birthday = data['birthday']
                # studentobj.ticket = data['ticket']
                # studentobj.groups = data['student_group']
                # studentobj.photo = data['photo']
                # student.save()
                studentobj.save()

                # redirect to students list
                messages.add_message(request, messages.ERROR,
                                     u'Студент %s успешно изменен!' % request.POST.get('first_name', '').strip())
                return HttpResponseRedirect(u'%s?status_message=Студент %s успешно изменен!' % (
                reverse('home'), request.POST.get('first_name', '').strip()))
            else:
                messages.add_message(request, messages.ERROR, 'Пожалуйста исправьте следующие ошибки')
                # render form with errors and previous user input
                return render(request, 'students/students_edit3.html',
                              {'errors': errors, 'student': student, 'group': group, 'groups': Group.objects.all().order_by('title')})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.add_message(request, messages.ERROR, u'Изменение студента %s отменено!'%request.POST.get('first_name', '').strip())
            return HttpResponseRedirect(u'%s?status_message=Изменение студента %s отменено!'%(reverse('home'),request.POST.get('first_name', '').strip()))

    else:
         # initial form render

        pk = pk
        student = Student.objects.get(pk=pk)
        group = student.student_group
        formatedDate = student.birthday.strftime('%Y-%m-%d')

        return render(request, 'students/students_edit3.html', {'student': student, 'formatedDate':formatedDate, 'group': group, 'groups': Group.objects.all().order_by('title') } )

# Валидация с PIL
def validate_file_extension(value):
    valid_extensions = ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']
    try:
        im = Image.open(value)
        ext = im.format.lower().split()
        resoult = list(set(valid_extensions) & set(ext))
        if resoult:
            return True
        else:
            pass
    except:
        return False

def validate_size(photo):
    filesize = (photo._size) / 1000
    if filesize == 0 or filesize > 2000:
        return False
    else:
        return True

