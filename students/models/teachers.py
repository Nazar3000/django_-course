# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Teacher(models.Model):
    '''Student Model'''
    class Meta(object):
        verbose_name = "Пеподаватель"
        verbose_name_plural = "Преподаватели"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Имя"
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Фамилия"
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="Отчество",
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name="Дата рождения",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name="Фото",
        null=True
    )




    notes = models.TextField(
        blank=True,
        verbose_name="Дополнительные заметки"
    )


    # Отображает имя преподавателя в админке
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)