from mozio_drawing_tool.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mozio',
        'USER': 'mozio',
        'PASSWORD': 'moziodjangoapp',
        'HOST': 'mozio-django-app-mysql-db.ckcjy5xii4eu.sa-east-1.rds.amazonaws.com',
        'PORT': '3306'
    }
}

# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['APP_DIRS'] = False
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader',
        ['django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader'])
]

INSTALLED_APPS += ('storages',)

AWS_STORAGE_BUCKET_NAME = 'mozio-django-app-staticfiles'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL