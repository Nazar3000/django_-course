# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
    '''Exam Model'''

    class Meta(object):
        verbose_name = u"Экзамен"
        verbose_name_plural = u"Экзамены"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Предмет"
    )

    date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=u"Дата и время"
    )


    student_group = models.ManyToManyField('Group',
                                      verbose_name=u"Группа",
                                      blank=False,
                                      null=True,
                                      )

    teacher = models.ForeignKey('Teacher',
        verbose_name=u"Преподаватель",
        blank=False,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Дополнительные заметки")





    def __unicode__(self):
        if self.teacher:
            return u"%s (%s %s)" % (self.title, self.teacher.first_name, self.teacher.last_name)
        else:
            return u"%s" % (self.title,)
