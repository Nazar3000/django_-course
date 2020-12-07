# -*- coding: utf-8 -*-
from django.db import models


class Resoult(models.Model):
    '''Resoult Model'''

    class Meta(object):
        verbose_name = u"Результ экзамена"
        verbose_name_plural = u"Результаты экзаменов"

    title = models.IntegerField(
        blank=False,
        null=True,
        verbose_name=u"Оценка"
    )

    student = models.OneToOneField('Student',
                                   verbose_name=u"Студент",
                                   blank=False,
                                   null=True,
                                   on_delete=models.SET_NULL)

    exam = models.OneToOneField('Exam',
                                verbose_name=u"Предмет",
                                blank=False,
                                null=True,
                                on_delete=models.SET_NULL)

    teacher = models.OneToOneField('Teacher',
                                   verbose_name=u"Преподаватель",
                                   blank=False,
                                   null=True,
                                   on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные заметки")

    def __unicode__(self):
        if self.student:
            return u"%s (%s %s %s %s)" % (
                self.title, self.student.first_name, self.student.last_name, self.teacher.first_name,
                self.teacher.last_name)
        else:
            return u"%s" % (self.title,)
