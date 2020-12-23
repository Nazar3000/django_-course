"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from django.conf.urls import patterns
from django.contrib import admin
from django.contrib.staticfiles import views
# from django.urls import re_path
from django.views.static import serve

from students.views.students import students_list, students_edit, students_delete
from students.views.students_add import students_add
from students.views.groups import groups_list, groups_add, groups_edit, groups_delete
from students.views.journal import journal
from students.views.exams import exams_list
from students.views.exams_resoult import resoult_list
from students.views.contact_admin import contact_admin
from students.views.test_view import StudentList





from  .settings import MEDIA_ROOT, DEBUG





urlpatterns = [
    url(r'^$', students_list, name='home'),
    url(r'^students/add/$', students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_edit, name='students_edit'),

    url(r'^students/(?P<sid>\d+)/delete/$', students_delete, name='students_delete'),

# Groups url
    url(r'^groups/$', groups_list, name='groups'),
    url(r'^groups/add/$', groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$',groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_delete, name='groups_delete'),
    url(r'^admin/', include(admin.site.urls)),

# journal
    url(r'^journal/$', journal, name='journal'),

# exams
    url(r'^exams/$', exams_list, name='exams'),

# exams_resoult
    url(r'^resoult/$', resoult_list, name='resoult'),

# contact_form
    url(r'^contact-admin/$', contact_admin, name='contact_admin'),
]

if DEBUG:
    # serve files from media folder

    urlpatterns += [url(r'^media/(?P<path>.*)$', serve,{
            'document_root': MEDIA_ROOT,
        })
    # urlpatterns += [url(r'^media/(?P<path>.*)$', serve,
    #     document_root=MEDIA_ROOT,
    # )
            ]
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

