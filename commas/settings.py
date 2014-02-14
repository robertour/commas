# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Django settings for commas project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' 
#        # or 'oracle'.
#        'ENGINE': 'django.db.backends.', 
#        # Or path to database file if using sqlite3.
#        'NAME': '',
#        # The following settings are not used with sqlite3:
#        'USER': '',
#        'PASSWORD': '',
#        # Empty for localhost through domain sockets or 
#        # '127.0.0.1' for localhost through TCP.
#        'HOST': '',
#        # Set to empty string for default.
#        'PORT': '',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'database.sqlite'),
    }
}

INTERNAL_IPS = ['127.0.0.1', '216.185.102.18']

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'localhost',
    '.commasindustry.com', # Allow domain and subdomains
    '.commasindustry.com.', # Also allow FQDN and subdomains
    '.commasindustry.my', # Allow domain and subdomains
    '.commasindustry.my.', # Also allow FQDN and subdomains
    '.commas.webfactional.com', # Allow domain and subdomains
    '.commas.webfactional.com.', # Also allow FQDN and subdomains
]



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Email for the contact form
DEFAULT_FROM_EMAIL = 'testcommas@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testcommas@gmail.com'
EMAIL_HOST_PASSWORD = 'discodisco'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = ''
# MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../media/').replace('\\', '/'))


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
#MEDIA_URL = ''
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = ''
# STATIC_ROOT = os.path.join(PROJECT_PATH, "../static/")
STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../static/').replace('\\', '/'))


# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@tt9_5g15r023+-t(3oxqn%##x-86ql6m$x42n_os-cgr17o@)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'commas.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'commas.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    # 'django_admin_bootstrapped',
    # 'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'avatar',
    'disqus',
    'compressor',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'widget_tweaks',
    #'cms.plugins.file',
    #'cms.plugins.flash',
    #'cms.plugins.googlemap',
    #'cms.plugins.link',
    #'cms.plugins.picture',
    #'cms.plugins.snippet',
    #'cms.plugins.teaser',
    'cms.plugins.text',
    #'cms.plugins.video',
    #'cms.plugins.twitter',
    'easy_thumbnails',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'reversion',
    'tagging',
    'tinymce',
    'zinnia_bootstrap',
    'zinnia',
    'cmsplugin_zinnia',
    'cmsplugin_contact',
    'cmsplugin_custom_contact',
    'plugins')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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


#Django Compressor
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# DJANGO CMS
CMS_TEMPLATES = (
    ('zinnia/base.html', 'Zinnia Blog'),
    ('about.html', 'About'),
    ('services.html', 'Services'),
    ('credentials.html', 'Credentials'),
    ('home.html', 'Home'),
    ('contact.html', 'Contact'),
    ('general.html', 'General')
)

CMS_PLACEHOLDER_CONF = {
    'credential': {
        'plugins': {'CredentialPlugin'}
    },
    'reference': {
        'plugins': {'ReferencePlugin'}
    },
    'reference-title': {
        'plugins': {'TextPlugin'}
    },
    'service': {
        'plugins': {'ServicePlugin'}
    },
    'team': {
        'plugins': {'TeamPlugin'}
    },
    'member': {
        'plugins': {'MemberPlugin'}
    },
    'about-image-header': {
        'plugins': { 'FilerImagePlugin' }
    }, 
    'service-image-header': {
        'plugins': { 'FilerImagePlugin' }
    }, 
    'main_logo': {
        'plugins': {'FilerImagePlugin'}
    },
    'home-background-image': {
        'plugins': { 'FilerImagePlugin' }
    },
    'home-teaser': {
        'plugins': { 'TextPlugin', 'EditorTextPlugin' }
    },
    'service-teaser': {
        'plugins': { 'TextPlugin', 'EditorTextPlugin' }
    },
    'social-share': {
        'plugins': { 'TextPlugin' }
    },
    'social-links': {
        'plugins': { 'TextPlugin' }
    },
    'contact_title': {
        'plugins': { 'TextPlugin', 'EditorTextPlugin' }
    },
    'contact_teaser': {
        'plugins': { 'TextPlugin', 'EditorTextPlugin' }
    },
    'customcontactform': {
        'plugins': {'CustomContactPlugin'}
    },
    'contactinfo': {
        'plugins': { 'TextPlugin', 'EditorTextPlugin' }
    },
    'custom-widgets-top': {
        'plugins': {'FilerVideoPlugin', 'FilerImagePlugin', 
        'TextPlugin', 'EditorTextPlugin', 'WidgetPlugin' }
    },
    'custom-widgets-middle': {
        'plugins': {'FilerVideoPlugin', 'FilerImagePlugin', 
        'TextPlugin', 'EditorTextPlugin', 'WidgetPlugin' }
    },
    'custom-widgets-bottom': {
        'plugins': {'FilerVideoPlugin', 'FilerImagePlugin', 
        'TextPlugin', 'EditorTextPlugin', 'WidgetPlugin' }
    },
    'content': {
        'plugins': {'FilerVideoPlugin', 'FilerFilePlugin',
        'FilerImagePlugin', 'TextPlugin', 'EditorTextPlugin' }
    },
    'the_css': {
        'plugins': { 'TextPlugin' }
    },
}

LANGUAGES = [
    ('en', 'English'),
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
#from easy_thumbnails.conf import Settings as thumbnail_settings
#THUMBNAIL_PROCESSORS = (

#) + thumbnail_settings.THUMBNAIL_PROCESSORS

ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'


TINYMCE_DEFAULT_CONFIG = {
    'theme' : "advanced",
    'mode' : "textareas",
    'width' : "100%",
    'relative_urls': False
}

#ZINNIA
ZINNIA_PAGINATION = 3

#DISQUS
#DISQUS_API_KEY = 'mXY3XEWpHL07bx6CYKK8vbgU4Kh1WveazeCSIsuViflNc2eTAXWA0SzJ5Nwh4f93'
DISQUS_API_KEY = '2YvuU4sEq9AtxiD4e6OQwku6Jc2Wy247MCg8z7WENHLgqOyemuvWgKFk5j383QUx'
DISQUS_WEBSITE_SHORTNAME = 'commasindustry'

# CMSPLUGIN_CONTACT
CMSPLUGIN_CONTACT_FORMS = (
    ('cmsplugin_contact.forms.ContactForm', 'default'),
    ('forms.ContactFormy', 'My form'),
)

#TINYMCE_JS_URL = os.path.join(MEDIA_ROOT, "js/tiny_mce/tiny_mce.js")
#TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "js/tiny_mce")
#TINYMCE_COMPRESSOR = True

# For the Blog
#CMSPLUGIN_BLOG_PLACEHOLDERS = ('first', 'second', 'third')
#JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
#JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
#JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'
# Feed it locally
#JQUERY_UI = '/path/to/jquery/'
#JQUERY_JS = '%sjs/jquery-1.4.4.min.js' % JQUERY_UI
#JQUERY_UI_JS = '%sjs/jquery-ui-1.8.9.custom.min.js' % JQUERY_UI
#JQUERY_UI_CSS = '%scss/smoothness/jquery-ui-1.8.9.custom.css' % JQUERY_UI
