# -*- coding: utf-8 -*-
from django.db import models
from ..util import paginate, get_current_group


class Resoult(models.Model):
    '''Resoult Model'''

    class Meta(object):
        verbose_name = "Результ экзамена"
        verbose_name_plural = "Результаты экзаменов"

    title = models.IntegerField(
        blank=False,
        null=True,
        verbose_name="Оценка"
    )

    student = models.OneToOneField('Student',
                                   verbose_name="Студент",
                                   blank=False,
                                   null=True,
                                   on_delete=models.SET_NULL)

    exam = models.OneToOneField('Exam',
                                verbose_name="Предмет",
                                blank=False,
                                null=True,
                                on_delete=models.SET_NULL)

    teacher = models.OneToOneField('Teacher',
                                   verbose_name="Преподаватель",
                                   blank=False,
                                   null=True,
                                   on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name="Дополнительные заметки")

    def __str__(self):
        if self.student:
            return "%s (%s %s %s %s)" % (
                self.title, self.student.first_name, self.student.last_name, self.teacher.first_name,
                self.teacher.last_name)
        else:
            return "%s" % (self.title,)
