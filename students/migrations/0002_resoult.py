# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resoult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.IntegerField(null=True, verbose_name='\u041e\u0446\u0435\u043d\u043a\u0430')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438', blank=True)),
                ('exam', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442', to='students.Exam')),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student')),
                ('teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', to='students.Teacher')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442 \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0430',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u043e\u0432',
            },
            bases=(models.Model,),
        ),
    ]
