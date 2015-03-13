"""
Django settings for feral project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(PYTHON_PATH, ...)
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
PYTHON_PATH = (os.path.split(SETTINGS_PATH))[0]
PROJECT_PATH = (os.path.split(PYTHON_PATH))[0]
ENV_PATH = (os.path.split(PROJECT_PATH))[0]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')(wmvr(nsr4$o71l7&wk+6e2o%k$l*2nog5srewdxsf%5x!%v&'

SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.redirects',

    # Other
    'polymorphic',
    'ckeditor',
    'easy_thumbnails',
    'mptt',
    'filer',
    'robots',

    # Custom
    'core',
    'project',
    'blog',
    'snippet',
    'flatpage',
    'menu'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    'menu.context_processors.menu'
)

MIGRATION_MODULES = {
    'filer': 'filer.migrations_django',
}

ROOT_URLCONF = 'feral.urls'

WSGI_APPLICATION = 'feral.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en-us', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ENV_PATH, 'static/')
STATICFILES_DIRS = (
    os.path.join(PYTHON_PATH, 'static/dist/'),
    os.path.join(PYTHON_PATH, 'static/bower_components/'),
    os.path.join(PYTHON_PATH, 'static/vendor/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

MEDIA_ROOT = os.path.join(ENV_PATH, "media")
MEDIA_URL = "/media/"

TEMPLATE_DIRS = (
    os.path.join(PYTHON_PATH, 'templates/'),
)

# CKEditor
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
            (
                ['Styles', 'Format', 'TextColor'],
                ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                    'Superscript', '-', 'RemoveFormat'],
                ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                    'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter',
                    'JustifyRight', 'JustifyBlock'],
                ['Cut', 'Copy', 'Paste', 'PasteText', '-', 'Undo', 'Redo'],
                ['Link', 'Unlink', 'Anchor'],
                ['Source', 'Maximize', 'ShowBlocks'],
            ),
        'startupOutlineBlocks': True,
        'width': '600px'
    },
}

# Suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'Feral Studio',
}
