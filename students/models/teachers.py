# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Teacher(models.Model):
    '''Student Model'''
    class Meta(object):
        verbose_name = u"Пеподаватель"
        verbose_name_plural = u"Преподаватели"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Имя"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Фамилия"
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"Отчество",
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата рождения",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True
    )




    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные заметки"
    )


    # Отображает имя преподавателя в админке
    def __unicode__(self):
        return u"%s %s" %(self.first_name, self.last_name)