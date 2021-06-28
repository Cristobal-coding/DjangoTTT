from unipath import Path
import json
from django.core.exceptions import ImproperlyConfigured
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open("secret.json")as f:
    secret = json.loads(f.read())
def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "La variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)


SECRET_KEY = get_secret('SECRET_KEY')


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'crispy_forms',

)
LOCAL_APPS = (
    'applications.users',
    'applications.home',
    'applications.alumnos',
    'applications.cursos',
    'applications.asignaturas',
)
THIRD_PARTY_APPS =(
    'crispy_forms',
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TrabajoTitulo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.request',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'TrabajoTitulo.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# SESSION_COOKIE_AGE = 30*60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
AUTH_USER_MODEL = 'users.user'
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'Chile/EasterIsland'

USE_I18N = True

USE_L10N = True

USE_TZ = True



