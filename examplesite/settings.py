# Django settings for examplesite project.
import logging
import os

LOCAL_FILE = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'v7=v0zj1id+d!e6zwqg4+w2mss_o1u$yvy2+p0%6w5azjnm1ma'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'examplesite.urls'

WSGI_APPLICATION = 'examplesite.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(LOCAL_FILE, "templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'press',
    'publish',
    'ckeditor',
    'django_nose',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INSTALLED_APPS = INSTALLED_APPS + (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

logging.disable(logging.CRITICAL)

PRESS_DEFAULT_WIDGET = 'ckeditor.widgets.CKEditorWidget'
CKEDITOR_UPLOAD_PATH = os.path.join(LOCAL_FILE, "ckupload")
CKEDITOR_CONFIGS = {
    'default': {
        'forcePasteAsPlainText': True,
        'pasteFromWordPromptCleanup': False,
        'uiColor': '#ffffff',
        'toolbar': [
            {'name': 'styles', 'items': [
                'Format', '-', 'Bold', 'Italic', 'Underline', 'Strike', '-',
                'RemoveFormat']},
            {'name': 'paragraph', 'items': [
                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'Blockquote', '-', 'SelectAll']},
            {'name': 'insert', 'items': [
                'Table', 'HorizontalRule', '-', 'Link', 'Unlink'
            ]}
        ]
    },
}

NOSE_ARGS = [
    '--nocapture',
    '--nologcapture',
    '--verbosity', '2',
]