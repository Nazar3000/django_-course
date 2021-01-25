# -*- coding: utf-8 -*-
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic.base import TemplateView
from ..models import MonthJournal, Student
from ..util import paginate



# Views for journal
class JournalView(TemplateView):
    template_name = 'students/journal.html'
    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(JournalView, self).get_context_data(**kwargs)
        # Разпринтить что входит вконтекст после вызова супер
        # попробовать отдельно запутстить этот модуль

        # проверяем передано ли месяц в параметре,
        # если нет - вычисляем текущий;
        # пока что отделяем текущий:


        # check if we need to display some specific month
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'], '%Y-%m-%d').date()

        else:
            # othrwise just displaying current month data
            today = datetime.today()
            month = date(today.year, today.month, 1)

        # вычисляем текущий год, предыдущий и следующий месяцы,
        # а пока выдаем их статично:
        # calculate current< previous and next month details;
        # we need this for month navigation element in template

        next_month = month + relativedelta(months=1)
        prev_month = month - relativedelta(months=1)
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')


        # context['prev_month'] = '2026-06-01'
        # context['next_month'] = '2026-08-01'
        # context['year'] = 2026

        # также теккущий месяц;
        # переменную cur_month мы используем позже
        # в пагинации; а month_verbose в навигации
        # помесячной:

        # we'll use this variable in students pagination
        context['cur_month'] = month.strftime('%Y-%m-%d')

        # context['cur_month'] = '2026-07-01'
        # context['month_verbose'] = u'Липень'

        # prepare variable for template to generate
        #     jornal table header elements
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [{'day': d,
                                    'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
                                   for d in range(1, number_of_days+1)]





        # тут будем вычислять список дней в месяце,
        # а пока забьем статично:
        # context['month_header'] = [
        #     {'day': 1, 'verbose': 'Пн'},
        #     {'day': 2, 'verbose': 'Вт'},
        #     {'day': 3, 'verbose': 'Ср'},
        #     {'day': 4, 'verbose': 'Чт'},
        #     {'day': 5, 'verbose': 'Пт'},
        # ]

        # вытягиваем всех студентов отсортированых по
        # queryset = Student.objects.order_by('last_name')
        # get all students from database
        queryset = Student.objects.all().order_by('last_name')

        # це адреса для посту AJAX запиту, як бачите, ми
          # робитимемо його на цю ж в’юшку; в’юшка журналу
          # буде і показувати журнал і обслуговувати запити
         # типу пост на оновлення журналу;
        # url to update student presence, for form post
        update_url = reverse('journal')

        # пройдемся по всех студентах и соберем
        # необходимые данные:
        # go over all students and collect data about presence
        # during selected month
        students = []
        for student in queryset:
            # TODO: вытаскиваем журнал для студента и выбраного месяца

            # try to get journal object by month selected
            # month and current student
            try:
                journal = MonthJournal.objects.get(student=student, date=month)

            except Exception:
                journal = None

            # fill in days presence list for current student
            days = []
            for day in range(1, number_of_days+1):

                days.append({
                    'day': day,
                    'present': journal and getattr(journal, 'present_day%d' % day, False) or False,
                    'date': date(myear, mmonth, day).strftime('%Y-%m-%d'),
                })

                # набиваем все отальные данные студента
                # prepare metadata for current student

            students.append({
                'fullname': u'%s %s'%(student.last_name, student.first_name),
                'days': days,
                'id': student.id,
                'update_url': update_url,
            })
            # students = queryset
                # применяем пагинацию к списку студентов
                # apply pagination, 10 students per page

        context = paginate(students, 3, self.request, context,
                           var_name='students')

        # возвращаем обновленный словарь с данными
        # finally return updated context
        # with paginated students
        return context

# def journal(request):
#     return render(request, 'students/journal.html')
