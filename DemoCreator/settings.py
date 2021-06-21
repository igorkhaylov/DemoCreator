"""
Django settings for DemoCreator project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@c0f^6msi(&dhic!%boy9&$m$8sh$xtvl(z3_z^i3xw-uwgbb&'

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
    'main.apps.MainConfig',
    'ckeditor',
    'ckeditor_uploader',
    'sorl.thumbnail',

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

ROOT_URLCONF = 'DemoCreator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'DemoCreator.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = "uploads/"

# CKEDITOR_CONFIGS = {
#     'skin': 'moono',
#     'default': {
#         'toolbar': 'full',
#     },
# }


CKEDITOR_CONFIGS = {
    'skin': 'moono',
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', "Youtube", "Image"]
        ],
        'extraPlugins': ','.join([
            'youtube',
        ]),
    },
    'my_config': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Source", "Templates", 'Format', 'Font', 'FontSize', 'Maximize', 'ShowBlocks'], '/',
            ['Image', 'Youtube', 'Table', 'Bold', 'Italic', 'Underline', 'Strike', 'Indent', 'Outdent',
             'HorizontalRule'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Blockquote', 'NumberedList'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            'youtube',
        ]),
    },
    'for_church': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Source", 'Font', 'FontSize', 'Maximize', 'ShowBlocks'], '/',
            ['Image', 'Youtube', 'Table', 'Bold', 'Italic', 'Underline', 'Strike', 'Indent', 'Outdent',
             'HorizontalRule'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Blockquote', 'NumberedList'],
            ['BulletedList', 'TextColor', 'BGColor', 'Link', 'Smiley', 'SpecialChar'], '/',
            ['Find', 'Subscript', 'Superscript'], '/',
            [], '/',
            [], '/',
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            'youtube',
        ]),
    },
}

# CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.2.1/jquery.min.js"
# CKEDITOR_IMAGE_BACKEND = "pillow"
