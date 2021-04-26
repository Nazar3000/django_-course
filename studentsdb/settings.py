"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf import global_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PORTAL_URL = 'http://localhost:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$lrm#z+qs)(&2rkr)tnui0m0%7r%)s!)9ni$#ug_vjmce+5x%!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'registration',
    'students',
    'stud_auth',
    'contact_form',
    'studentsdb',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'

# Content validation

CONTENT_TYPE = ['image', 'video']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "2000000"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# We moved DATABASES variable to db.py module which added to .gitignore
# so we don't keep mysql passwords in repository
from .db import DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'
DATE_FORMAT = "%Y-%m-%d"

USE_I18N = True

USE_L10N = True


USE_TZ = True
LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_List = {
    'en':{'title':'EN'},
    'uk':{'title':'UK'},
    'ru':{'title':'RU'}
}

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('uk', gettext('Ukrainian')),
    ('ru', gettext('Russian')),
)
# MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'uk', 'ru')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "studentsdb.context_processors.students_proc",
    "students.context_processors.groups_processor",
    "students.context_processors.lang_processor",
    "studentsdb.context_processors.users_proc",
)

# AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
# )

# email settings
ADMIN_EMAIL = 'nazarii.mazur@gmail.com'
EMAIL_HOST = 'smtp.ukr.net'
EMAIL_PORT = '2525'
EMAIL_HOST_USER = 'django_admin@ukr.net'
EMAIL_HOST_PASSWORD = 'Qwerty!123'
EMAIL_USE_TLS= True



# add project templates directory as Django does not
# pick it default
# TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'studentsdb', 'templates'),
# )


TEMPLATE_DIRS = (
   os.path.join(BASE_DIR,
                'templates',
                # 'registration'
                ),
)

# TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'students/templates', 'students' ),
# )



LOG_FILE = os.path.join(BASE_DIR, 'studentdb.log')

# django-registration-redux settings
REGISTRATION_OPEN =True
LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logoun'

LOGGING = {
    'version': 1,
    'disable_existing_loggers' :True,
    'formatters': {
        'verbose':{
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        },
        'simple':{
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers':{
        'null':{
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file':{
            'level':'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
    },
    'loggers':{
        'django':{
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'students.signals':{
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'students.views.contact_admin':{
            'handlers':['console', 'file'],
            'level': 'INFO',
        }
    }
}
