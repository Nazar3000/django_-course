# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_phone', models.CharField(default=b'', max_length=12, verbose_name='Mobile Phone', blank=True)),
                ('actual_address', models.CharField(default=b'', max_length=20, verbose_name='Actual address', blank=True)),
                ('passportID', models.CharField(default=b'', max_length=20, verbose_name='Passport ID', blank=True)),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
            bases=(models.Model,),
        ),
    ]
