import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

# hosts
ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER':  os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST':  os.environ.get('DATABASE_HOST'),
    }
}