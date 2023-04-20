"""
Django settings for DETECTA project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^e7zg)fq-vg5@e7w9xu^#6=%3r30%k6mp3b6v$6q^4@a+#i4$g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',#Importando las interfaces del sistema administrativo plugin Jazzmin
    'admin_interface',#Importando las interfaces del sistema administrativo
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Academia',
    'colorfield',#Importando los colores del sistema administrativo
]

X_FRAME_OPTIONS = 'SAMEORIGIN'


#Settings Jazzmin
JAZZMIN_SETTINGS = {
     # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "DETECTA",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": 'DETECTA',
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/img/detectaAdmin.png",
     # Copyright on the footer
    "copyright": "Academia DETECTA",
    # Logo to use for login form in dark themes (defaults to login_logo)
    #"login_logo_dark": None,
    # Welcome text on the login screen
    "welcome_sign": "Bienvenido a la Academia DETECTA",
    'icons': {
    'Academia.Cursos': 'fas fa-book',
    'Academia.Alumnos': 'fas fa-user-graduate',
    'Academia.Profesor': 'fas fa-chalkboard-teacher',
    'Academia.Proveedor': 'fas fa-truck',
    'Academia.TelefonoAlumno': 'fas fa-phone',
    'Academia.EmailAlumno': 'far fa-envelope',
    'Academia.TelefonoProfesor': 'fas fa-phone',
    'Academia.EmailProfesor': 'far fa-envelope',
    'Academia.TelefonoProveedor': 'fas fa-phone',
    'Academia.EmailProveedor': 'far fa-envelope',
    'Academia.Materiales': 'fas fa-chalkboard',
    'Academia.MediosDidacticos': 'fas fa-laptop',
    'Academia.AlumnoCurso': 'fas fa-graduation-cap',
    'auth.user': 'fas fa-user',
    'auth.group': 'fas fa-users',
    'admin_interface.temes': 'fas fa-paint-brush'
    },
    
    "topmenu_links": [
        #{'app': 'Academia'},
        {'models': 'Academia.Alumnos.Alumnos'},
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {   'type': 'url',
            'name': 'Inicio',
            'url': 'http://127.0.0.1:8000',
            "icon": "fas fa-house",
        }
    ]
}

JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
}
#JAZZMIN_UI_TWEAKS = {
    #"theme": "custom",
    #"show_switch_theme": True,  # permite al usuario cambiar entre temas
    #"custom_css": "css/custom.css",
#}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DETECTA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'DETECTA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DETECTA',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'piam2023',
        'PORT': '5432',
        #'OPTIONS': {
        #    'driver': 'ODBC Driver 17 for SQL Server',
        #},
    },
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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/Academia/static/'

import os
MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
