import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'studentsdb',

        'USER': 'studentsdb',

        'PASSWORD': '1q2w3e4r5t6y',

        'HOST': 'localhost',

        'PORT': '',

    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': 'localhost',
    #     'USER': 'students_db_user',
    #     'PASSWORD': 'password',
    #     'NAME': 'students_db',
    # }

}
