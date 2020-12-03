import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
# 'default': {
#
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#
#         'NAME': 'students_db',
#
#         'USER': 'students_db_user',
#
#         'PASSWORD': 'password',
#
#         'HOST': 'localhost',
#
#         'PORT': '5432',
#
#     }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': 'password',
        'NAME': 'students_db',
    }

}
