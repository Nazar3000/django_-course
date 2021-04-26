# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsdb', '0002_stprofile_actual_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='stprofile',
            name='passportID',
            field=models.CharField(default=b'', max_length=20, verbose_name='Passport ID', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stprofile',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True),
            preserve_default=True,
        ),
    ]
