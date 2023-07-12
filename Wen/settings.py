"""
Django settings for Wen project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8#rchxzea9!8xs+h7e_je1h-eo^otkws7ull*yx55c$bdm)$n='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'login',
    'inicio_sesion',
    'curso',
    'blog',
    'videos',
    'micontenido',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Wen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Wen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wendev',
        'USER': 'ibm_cloud_ddb7036a_5af4_4989_b53b_72aabb3d6471',
        'PASSWORD': '2f1d95edd45add0b2ce96c93f852eb14d8a1e547f437aae2dbd748bf357f3975',
        'HOST': '2f84f822-1b65-4213-a47d-784494cd5cc0.btdkfu0w0p0vutjk0r9g.databases.appdomain.cloud',
        'PORT': '30860',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = ['https://gwenluy.com',]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
 
STATIC_URL = 'static/'
STATIC_ROOT =  os.path.join(BASE_DIR,'static') 
MEDIA_URL= '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR,'media')

MERCADO_PAGO_CLIENT_ID = 'TEST-45f25815-70b7-4017-9052-2bb2a4acdcfa'
MERCADO_PAGO_CLIENT_SECRET = 'TEST-13674068714057-062721-6a711bd620175aa9edb5aec2d47ec6d3-1091690075'

#paypal
CLIENT_ID = "AeB5FOIGIoRzw4PQkpM4wg0CWW9NOSJrV2oJCUtdhOusKa0F2jqz_rT5QlC2m7XxrKmHSIUiYik7ksb8"
CLIENT_SECRET = "EDPOiRQwhbfzk3qO0o4PxriQpqiCWHy6RpYnM1cOumK_J_mTy8kHmCPAEeBfL47_-JC0Hqmb2NoLiRP6"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
