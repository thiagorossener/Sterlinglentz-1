from .default import *

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'feral_local',
        'USER': 'feral_user',
        'PASSWORD': 'staging',
    }
}

INSTALLED_APPS += ('debug_toolbar',)
