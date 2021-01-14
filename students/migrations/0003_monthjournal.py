# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_resoult'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('student', models.ForeignKey(unique_for_month=b'date', verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0439 \u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0435 \u0436\u0443\u0440\u043d\u0430\u043b\u044b',
            },
            bases=(models.Model,),
        ),
    ]
