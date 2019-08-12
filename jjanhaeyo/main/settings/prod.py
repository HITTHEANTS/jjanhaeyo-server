from os import environ


ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = []
origin = environ.get('JJANHAEYO_ORIGIN')
if origin:
    CSRF_TRUSTED_ORIGINS.append(origin)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'NAME': environ.get('JJANHAEYO_DB_NAME', 'jjanhaeyo'),
        'USER': environ.get('JJANHAEYO_DB_USER', 'root'),
        'PASSWORD': environ.get('JJANHAEYO_DB_PASSWORD', ''),
        'HOST': environ.get('JJANHAEYO_DB_HOST', 'localhost'),
        'PORT': environ.get('JJANHAEYO_DB_PORT', '3306'),
    }
}
