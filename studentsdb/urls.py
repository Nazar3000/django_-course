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
# from django.conf.urls import include, url
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
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
# from django.views.i18n import javascript_catalog #in django 1.7
from django.views.i18n import JavaScriptCatalog

from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from stud_auth.views.registration_custom import LoginFormView, LoginForm, RegistrationViewCustom
from stud_auth.views.user_profile import UserProfileView
# from vi
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required
from registration.backends.simple import urls as reg_urls


from  .settings import MEDIA_ROOT, DEBUG, MEDIA_URL

js_info_dict = {
    'packages':('students',),
}



urlpatterns = [
 # User Related urls
    #  можно добавить урлконфиг accounts/login/ и передать в него путь к шаблону который будет юзатся,
    # мо умолчанию шаблон тянется из registration/login.html
    # url(r'accounts/login/$', auth_views.login, kwargs={'template_name':'registration/login.html'}),
    # url(r'accounts/login/$', LoginFormView.as_view()),
    # первый неоч красивый вариант реализации сcrispy_forms
    # url(r'^users/login/$ ', auth_views.login, kwargs={'authentication_form':LoginForm,'template_name':'registration/crpy_login.html' }, name='login'),
    # Второй нормальный вариант реализации сcrispy_forms
    path('users/login/', LoginFormView.as_view(), name='login'),
    # Форма регистрации реализация с сcrispy_forms
    path('users/register/', RegistrationViewCustom.as_view(), name='register'),

    path('users/logout/', auth_views.LogoutView.as_view(next_page='home'), name='auth_logout'),
# User Profile
    path('users/profile/', login_required(TemplateView.as_view(template_name='registration/profile.html')),
        name='profile'),
    path('users/profile/<int:pk>', login_required(UserProfileView.as_view()),
        name='profile2'),

    path('register/complete/', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    path('users/', include((reg_urls, 'users'), namespace='users')),
    # path('users/', include(('registration.backends.simple.urls', 'users'), namespace='users')),


    # url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),
    path('jsi18n/', JavaScriptCatalog.as_view(packages=['students']),
         name='javascript-catalog'),

    # Students Urls
    path('', students_list, name='home'),
    path('students/add/', students_add, name='students_add'),
    # url(r'^students/add2/&', AddStudents.as_view(), name='students_add2'),
    # url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    path('students/<int:pk>/edit3/', students_edit3, name='students_edit3'),
    path('students/edit2/<int:pk>', Students_edit.as_view(), name='students_edit2'),


    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='students_delete'),
    path('students/<int:pk>/delete3/', students_delete, name='students_delete3'),

# Groups url

    path('groups/', login_required(groups_list), name='groups'),
    path('groups/add/', AddGroup.as_view(), name='groups_add'),
    path('groups/<int:pk>/edit/', GroupUpdateView.as_view(), name='groups_edit'),
    path('groups/<int:pk>/delete/', GroupsDeleteView.as_view(), name='groups_delete'),
    path('admin/', admin.site.urls),

# journal
    re_path(r'journal/(?:(?P<pk>\d+)/)?$', JournalView.as_view(), name='journal'),

# exams
    path('exams/', login_required(exams_list), name='exams'),
    path('exams/<int:pk>/edit/', ExamsUpdateView.as_view(), name='exams_edit'),
    path('exams/add/', AddExam.as_view(), name='exam_add'),
    path('exams/<int:pk>/delete/', ExamDeleteView.as_view(), name='exam_delete'),

# exams_resoult
    path('resoult/', login_required(resoult_list), name='resoult'),

# contact_form
#     url(r'^contact-admin/$', contact_admin, name='contact_admin'),
    path('contact-admin/', ContactView.as_view(), name='contact_admin'),

    path('test-form/', Test_form.as_view(), name='test-form'),



] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += i18n_patterns(
    # '',
path('students/add2/', AddStudents.as_view(), name='students_add2'),
path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='students_edit'),

)

# if DEBUG:
#     # serve files from media folder
#
#     urlpatterns += [url(r'^media/(?P<path>.*)$', serve,{
#             'document_root': MEDIA_ROOT,
#         })
    # urlpatterns += [url(r'^media/(?P<path>.*)$', serve,
    #     document_root=MEDIA_ROOT,
    # )
    #         ]
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

