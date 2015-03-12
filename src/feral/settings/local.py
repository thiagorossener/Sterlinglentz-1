from .default import *

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PYTHON_PATH, 'db.sqlite3'),
    }
}

INSTALLED_APPS += ('debug_toolbar',)
