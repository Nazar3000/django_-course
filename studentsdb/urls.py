# -*- coding: utf-8 -*-
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

from students.views.students import students_list, students_edit, StudentUpdateView, StudentDeleteView
from students.views.students_add import students_add
from students.views.groups import groups_list, AddGroup, GroupUpdateView, GroupsDeleteView
from students.views.journal import JournalView
from students.views.exams import exams_list, ExamsUpdateView, AddExam, ExamDeleteView
from students.views.exams_resoult import resoult_list
from students.views.contact_admin import ContactView
# ,contact_admin

from students.views.test_form import Test_form
from students.views.students_edit2 import Students_edit
from students.views.student_add2 import AddStudents
from students.views.students_edit3 import students_edit3
from students.views.students_delete3 import students_delete
from django.views.i18n import javascript_catalog
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from students.views.registration_custom import LoginFormView, LoginForm, RegistrationViewCustom
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required


from  .settings import MEDIA_ROOT, DEBUG

js_info_dict = {
    'packages':('students',),
}



urlpatterns = [
    url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^$', students_list, name='home'),
    url(r'^students/add/$', students_add, name='students_add'),
    # url(r'^students/add2/&', AddStudents.as_view(), name='students_add2'),
    # url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/edit3/$', students_edit3, name='students_edit3'),
    url(r'^students/edit2/(?P<pk>\d+)', Students_edit.as_view(), name='students_edit2'),


    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),
    url(r'^students/(?P<pk>\d+)/delete3/$', students_delete, name='students_delete3'),

# Groups url

    url(r'^groups/$', login_required(groups_list), name='groups'),
    url(r'^groups/add/$', AddGroup.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupsDeleteView.as_view(), name='groups_delete'),
    url(r'^admin/', include(admin.site.urls)),

# journal
    url(r'^journal/(?P<pk>\d+)?/?$', login_required(JournalView.as_view()), name='journal'),

# exams
    url(r'^exams/$', login_required(exams_list), name='exams'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamsUpdateView.as_view(), name='exams_edit'),
    url(r'^exams/add/$', AddExam.as_view(), name='exam_add'),
    url(r'^exams/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view(), name='exam_delete'),

# exams_resoult
    url(r'^resoult/$', login_required(resoult_list), name='resoult'),

# contact_form
#     url(r'^contact-admin/$', contact_admin, name='contact_admin'),
    url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),

    url(r'test-form/&', Test_form.as_view(), name='test-form'),


    # User Related urls
    #  можно добавить урлконфиг accounts/login/ и передать в него путь к шаблону который будет юзатся,
    # мо умолчанию шаблон тянется из registration/login.html
    # url(r'accounts/login/$', auth_views.login, kwargs={'template_name':'registration/login.html'}),
    # url(r'accounts/login/$', LoginFormView.as_view()),
    # первый неоч красивый вариант реализации сcrispy_forms
    # url(r'^users/login/$ ', auth_views.login, kwargs={'authentication_form':LoginForm,'template_name':'registration/crpy_login.html' }, name='login'),
    # Второй нормальный вариант реализации сcrispy_forms
    url(r'^users/login/$', LoginFormView.as_view(), name='login'),
    # Форма регистрации реализация с сcrispy_forms
    url(r'^users/register/$', RegistrationViewCustom.as_view(), name='register'),

    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

]

urlpatterns += i18n_patterns(
    '',
url(r'^students/add2/&', AddStudents.as_view(), name='students_add2'),
url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),

)

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

