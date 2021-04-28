# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _



class MonthJournal(models.Model):
    ''' Student Monthly Journal'''

    class Meta:
        verbose_name = _("Monthly Journal")
        verbose_name_plural = _("Monthly Journals")

    # list of days, each says whether student was presene or not
    key = ['present_day' + str(x) for x in range(1, 32)]
    for label in key:
        locals()[label] = models.BooleanField(default=False)

    student = models.ForeignKey('Student',
                                verbose_name=_("Student"),
                                blank=False,
                                unique_for_month='date',
                                on_delete=models.CASCADE)

    # we only need year and month, so always set day to first day of the month

    date = models.DateField(
        verbose_name=u'Дата',
        blank=False
    )

    # for i in range(1, 32):
    #     key = 'present_day' + str(i)
    #     value = models.BooleanField(default=False)
    #     setattr(MonthJournal, key, value)

    # list of days, each says whether student was presene or not
    # present_day1 = models.BooleanField(default=False)
    # present_day2 = models.BooleanField(default=False)
    # present_day3 = models.BooleanField(default=False)
    # present_day4 = models.BooleanField(default=False)
    # present_day5 = models.BooleanField(default=False)
    # present_day6 = models.BooleanField(default=False)
    # present_day7 = models.BooleanField(default=False)
    # present_day8 = models.BooleanField(default=False)
    # present_day9 = models.BooleanField(default=False)
    # present_day10 = models.BooleanField(default=False)
    # present_day11 = models.BooleanField(default=False)
    # present_day12 = models.BooleanField(default=False)
    # present_day13 = models.BooleanField(default=False)
    # present_day14 = models.BooleanField(default=False)
    # present_day15 = models.BooleanField(default=False)
    # present_day16 = models.BooleanField(default=False)
    # present_day17 = models.BooleanField(default=False)
    # present_day18 = models.BooleanField(default=False)
    # present_day19 = models.BooleanField(default=False)
    # present_day20 = models.BooleanField(default=False)
    # present_day21 = models.BooleanField(default=False)
    # present_day22 = models.BooleanField(default=False)
    # present_day23 = models.BooleanField(default=False)
    # present_day24 = models.BooleanField(default=False)
    # present_day25 = models.BooleanField(default=False)
    # present_day26 = models.BooleanField(default=False)
    # present_day27 = models.BooleanField(default=False)
    # present_day28 = models.BooleanField(default=False)
    # present_day29 = models.BooleanField(default=False)
    # present_day30 = models.BooleanField(default=False)
    # present_day31 = models.BooleanField(default=False)

   # varian for django 1.7

    # def __unicode__(self):
    #     return u'%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)

    # New variant
    def __str__(self):
        return '%s: %d, %d' % (self.student.last_name, self.date.month,
                               self.date.year)

# for i in range(1, 32):
#         key = 'present_day' + str(i)
#         value = models.BooleanField(default=False)
#         setattr(MonthJournal, key, value)

# key = ['present_day'+str(x) for x in range(1, 32)]
# for fild in key:
#     MonthJournal.add_to_class(fild, models.BooleanField(default=False))

