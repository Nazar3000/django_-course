# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210325_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='birthday_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthday_ru',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthday_uk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='photo_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='photo_ru',
        ),
        migrations.RemoveField(
            model_name='student',
            name='photo_uk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_group_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_group_ru',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_group_uk',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ticket_en',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ticket_ru',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ticket_uk',
        ),
    ]
