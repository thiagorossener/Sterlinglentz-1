from .default import *
from .private import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PRODUCTION_DB_NAME,
        'USER': PRODUCTION_DB_USER,
        'PASSWORD': PRODUCTION_DB_PASSWORD,
    }
}

ALLOWED_HOSTS = ("www.sterlinglentz.com", "sterlinglentz.com", "104.236.186.246")
