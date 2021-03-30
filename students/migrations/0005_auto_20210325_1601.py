# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20210113_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AddField(
            model_name='student',
            name='birthday_en',
            field=models.DateField(null=True, verbose_name='Birthday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='birthday_ru',
            field=models.DateField(null=True, verbose_name='Birthday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='birthday_uk',
            field=models.DateField(null=True, verbose_name='Birthday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='first_name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='first_name_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='first_name_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Last Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='Last Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='Last Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name_en',
            field=models.CharField(default=b'', max_length=256, null=True, verbose_name='Father name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name_ru',
            field=models.CharField(default=b'', max_length=256, null=True, verbose_name='Father name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name_uk',
            field=models.CharField(default=b'', max_length=256, null=True, verbose_name='Father name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='notes_en',
            field=models.TextField(null=True, verbose_name='Additional Notes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='notes_ru',
            field=models.TextField(null=True, verbose_name='Additional Notes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='notes_uk',
            field=models.TextField(null=True, verbose_name='Additional Notes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='photo_en',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='photo_ru',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='photo_uk',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='student_group_en',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='student_group_ru',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='student_group_uk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='ticket_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Ticket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='ticket_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='Ticket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='ticket_uk',
            field=models.CharField(max_length=256, null=True, verbose_name='Ticket'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=b'', max_length=256, verbose_name='Father name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(verbose_name='Additional Notes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='Ticket'),
            preserve_default=True,
        ),
    ]
