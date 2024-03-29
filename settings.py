# Django settings for readthebill project.
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://assets.sunlightfoundation.com/admin/1.2.5/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'gatekeeper.middleware.GatekeeperMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'readthebill.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.flatpages',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'mediasync',
    'gatekeeper',
    'failwhale',
    'feedinator',
    'morsels',
    'contact_form',
    'simplesurvey',
    'uspolitics.politicians',
    #'callingtool',
    #'capcall', #temporary
    'readthebill.rtb',
    'tagging',
    'blogdor',
    'gunicorn',
)

GATEKEEPER_ENABLE_AUTOMODERATION = True
GATEKEEPER_DEFAULT_STATUS = 0

CONTACT_FORM_RECIPIENTS = ['']

EMAIL_HOST = ""
EMAIL_PORT = "25"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True

MEDIASYNC = {
    'BACKEND': '',
    'AWS_KEY': '',
    'AWS_SECRET': '',
    'AWS_BUCKET': '',
    'AWS_PREFIX': 'rtb/2.0',
    'DOCTYPE': 'html5',
    'CACHE_BUSTER': 201103181119,
    'JOINED': {
        'css/readthebill.css': ('css/screen.css','css/rtb.css'),
        'js/readthebill.js': ('js/jquery-1.2.6.min.js','js/jquery.tablesorter.js'),
    },
}

import re
RTB_TAGS = ["72[\-\s]hour","read\s?the\s?bill", "h.\s?res. 504", "[^\w]?rtb[^\w]?"]
RTB_REGEX = [re.compile(r) for r in RTB_TAGS]
RTB_APPROVE_ALL = False

try:
    from local_settings import *
except ImportError, exp:
    pass
