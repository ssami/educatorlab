# Django settings for mainlab project.

import os 

#DEV = False # default is production where nothing is broken
#if (os.path.isfile("../.env-prod")) :
#	DEV = False

MAINTENANCE = False

if MAINTENANCE: 
	INDEX_FILE = "index_maintenance.html" 
else: 
	INDEX_FILE = "index.html"

DEV = True
if DEV:
	DEBUG = TEMPLATE_DEBUG = True

else : 
	DEBUG = TEMPLATE_DEBUG = False

ADMINS = (
	('Arvind Chandrababu', 'arvind.chandrababu@gmail.com'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if DEV : 
	DBNAME = "testeducatorlab"
else : 
	DBNAME = "educatorlab"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DBNAME,                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'educatorlab',
        'PASSWORD': 'tagoreinitiative',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["http://www.educatorlab.com"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

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
if DEV:
	MEDIA_ROOT = '/home/sumitasami/webapps/test_media/'
else : 
	MEDIA_ROOT = '/home/sumitasami/webapps/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
if DEV:
	MEDIA_URL = 'http://tagoreinitiative.com/media/'
else:
	MEDIA_URL = 'http://educatorlab.com/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"i
if DEV:
	STATIC_ROOT = '/home/sumitasami/webapps/test_static/'
else:
	STATIC_ROOT = '/home/sumitasami/webapps/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"

if DEV:
	STATIC_URL = 'http://tagoreinitiative.com/static/'
else:
	STATIC_URL = 'http://educatorlab.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	#'/home/sumitasami/webapps/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
	'dajaxice.finders.DajaxiceFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5&yflik$oxaf@xk&bv9=&1$r0pmp1y-b996$m@$6plhww85r+y'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mainlab.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mainlab.wsgi.application'

if DEV : 
	TEMPLATE = "/home/sumitasami/webapps/test_educator_lab/mainlab/templates"
else :
	TEMPLATE = "/home/sumitasami/webapps/educator_lab/mainlab/templates"	

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	
	TEMPLATE,
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	#dajax
	'dajaxice',
	'dajax',
	#django-ratings
	'djangoratings',
	#'django_admin_bootstrapped',
	'grappelli.dashboard',
	'grappelli',
    # Uncomment the next line to enable the admin:
	'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
	'django.contrib.admindocs',
	'mainlab',
    #the html editor in the admin interface
	'tinymce',
    #the DB migration tool
	'south',
)

TINYMCE_DEFAULT_CONFIG ={
    'theme' : 'advanced', 
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_buttons1': "bold,italic,underline,separator,bullist,separator,outdent,indent,separator,undo,redo",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_statusbar_location' : 'none',
	'plugins': 'paste'
}

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
        },
	'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
	'dajaxice' : {
            'handlers' : ['console'],
            'level' : 'WARNING',
            'propagate' : True,
    	},
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'qjyyrcoixyknmzhe'
EMAIL_HOST_USER = 'educatorlab@gmail.com'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'educatorlab@gmail.com'
SERVER_EMAIL = 'educatorlab@gmail.com' 


# Context Processors for the Grappelli Custom Dashboard 
# See http://django-grappelli.readthedocs.org/en/latest/dashboard_setup.html for more details

TEMPLATE_CONTEXT_PROCESSORS = (
    # "django.contrib.auth.context_processors.auth",
    # "django.core.context_processors.request",
    # "django.core.context_processors.i18n",
    # 'django.contrib.messages.context_processors.messages',
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.request',
        'django.contrib.messages.context_processors.messages'
)


AUTH_USER_MODEL = 'mainlab.MyUser'

GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

if DEV:
	SITE_URL = "http://tagoreinitiative.com/"
else: 
	SITE_URL = "http://educatorlab.com/"
	
# Close the session when user closes the browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Set time zone to Indian Standard Time
TIME_ZONE = 'Asia/Kolkata'