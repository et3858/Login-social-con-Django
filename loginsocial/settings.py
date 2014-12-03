"""
Django settings for loginsocial project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+$6cx!06q7htzhbki)#z%3sepgn&kt7#s7b&+q)#4p(*^z@f^f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # LEE ESTO: la siguiente linea es una instruccion para llamar a una libreria python para la ejecucion del Login Social
    'social.apps.django_app.default',
    # Primero que todo, si tienen instalado python y pip (el cual es un manejador de paquetes de python) entonces con pip instalen python-social-auth
    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'loginsocial.urls'

WSGI_APPLICATION = 'loginsocial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'





# Habiendo dclarado 'social.apps.django_app.default' en INSTALLED_APPS, entonces declaramos una variable llamada AUTHENTICATION_BACKENDS con las siguientes instrucciones
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    #'social.backends.linkedin.LinkedinOAuth1',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',#Autentificacion de sesion por defecto con usuario y contrasena
)


# Redireccion despues  de haber iniciado la sesion de usuario con login Social
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = '(miLlaveDeAutenticacionDeMiAplicacionDeTwitter)'
SOCIAL_AUTH_TWITTER_SECRET = '(miLlaveSecretaDeMiAplicacionDeTwitter)'

SOCIAL_AUTH_FACEBOOK_KEY = '(miLlaveDeAutenticacionDeMiAplicacionDeFacebook)'
SOCIAL_AUTH_FACEBOOK_SECRET = '(miLlaveSecretaDeMiAplicacionDeFacebook)'