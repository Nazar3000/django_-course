# -*- coding: utf-8 -*-
from django import forms
from django.contrib import messages
import os
from django.template.defaultfilters import filesizeformat
# from __future__ import unicode_literals
from django.conf import settings
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



import magic
import tempfile
from PIL import Image


from ..helpers.pagination import Pagination, EmptyPage, PageNotAnInteger
from ..models import Student, Group


# Декоратор для ограничения доступа дял не залогиненых пользвоателей
@login_required
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
                errors['first_name_id'] = "Имя"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия тоже есть обязательной"
                errors['last_name_id'] = "Фамилия"
            else:
                data['last_name'] = last_name

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
            # data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета есть обязательным"
                errors['ticket_id'] = "Билет"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу для студента"
                errors['student_group_id'] = "Группа"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) !=1:
                    errors['student_group'] = u"Выберите коректную группу"
                    errors['student_group_id'] = "Группа"

                else:
                    data['student_group'] = groups[0]


            # Валидация фото без Pillow
            photo = request.FILES.get('photo')

            if photo:

                validate_type=validate_file_extension(photo)
                data_type=type(photo)
                if validate_type is True:
                    validate=validate_size(photo)
                    if validate is True:
                        data['photo'] = photo
                    else:
                        errors['photo'] = u"Фото должно быть не больше 2 мб и не меньше 1 кб"
                        errors['photo_id'] = "Фото"

                else:
                    errors['photo'] = u"Это не фото, ты ошибся"
                    errors['photo_id'] = "Фото"




            # Валидация с python-magic
            # photo = request.FILES.get('photo')
            # if photo:
            #     validate_type=validate_file_extension(photo)
            #     if validate_type is True:
            #         validate=validate_size(photo)
            #         if validate is True:
            #             data['photo'] = photo
            #         else:
            #             errors['photo'] = u"Фото должно быть не больше 2 мб и не меньше 1 кб"
            #     else:
            #         errors['photo'] = u"Это не фото, ты ошибся"





            # # Валидация фото Django функционалом
            # photo = request.FILES.get('photo')
            # if photo:
            #     validate_content(photo)


            # save studen
            if not errors:
                student = Student(**data)
                student.save()

                # redirect to students list
                messages.add_message(request, messages.ERROR, u'Студент %s успешно добавлен!'%request.POST.get('first_name', '').strip())
                return  HttpResponseRedirect(u'%s?status_message=Студент %s успешно добавлен!'%(reverse('home'), request.POST.get('first_name', '').strip()))
            else:
                messages.add_message(request, messages.ERROR, 'Пожалуйста исправьте следующие ошибки')
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups':Group.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            messages.add_message(request, messages.ERROR, u'Добавление студента %s отменено!'%request.POST.get('first_name', '').strip())
            return HttpResponseRedirect(u'%s?status_message=Добавление студента %s отменено!'%(reverse('home'),request.POST.get('first_name', '').strip()))

    else:
         # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})






# def validate_file_extension(value):
#     ext = os.path.splitext(value.name)[1]
#     valid_extensions = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']
#     if not ext.lower() in valid_extensions:
#         return False
#     else:
#         return True



# Валидация с python-magic

# def validate_file_extension(value):
#     valid_extensions = ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']
#
#     ext=magic.from_buffer(value.read())
#     ext=ext.lower().split()
#     resoult=list(set(valid_extensions) & set(ext))
#     if resoult:
#         return True
#     else:
#         return False

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


# def validate_content(photo):
#     content = photo
#     content_type = content.content_type.split('/')[0]
#     if content_type > settings.CONTENT_TYPE:
#         if content._size >settings.MAX_UPLOAD_SIZE:
#             raise forms.ValidationError(_('Приведите загружаемое фото не более чем %s. Текущий размер %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
#     else:
#         raise forms.ValidationError(_('Это не фото'))
#     return content