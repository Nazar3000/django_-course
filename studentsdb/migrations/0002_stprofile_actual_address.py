# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stprofile',
            name='actual_address',
            field=models.CharField(default=b'', max_length=20, verbose_name='Actual address', blank=True),
            preserve_default=True,
        ),
    ]
