from .default import *
from .private import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'feral_staging',
        'USER': 'feral_user',
        'PASSWORD': 'staging',
    }
}

INSTALLED_APPS += ('debug_toolbar',)

ALLOWED_HOSTS = ("feral.timmyomahony.com",)
