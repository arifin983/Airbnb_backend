import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Define the base directory for the project (two levels up from settings.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Path to the .env.dev file
dotenv_path = BASE_DIR / '.env.dev'

# Load environment variables from .env.dev
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG", default=0)))

ALLOWED_HOSTS = [
    "localhost", 
    "127.0.0.1",
    "arifbnb.netlify.app",
    "airbnbbackend-production.up.railway.app"
]

AUTH_USER_MODEL = 'useraccount.User'

SITE_ID = 1

# if DEBUG:
#     WEBSITE_URL = 'http://localhost:8000'
# else:
WEBSITE_URL = 'https://airbnbbackend-production.up.railway.app'



AUTH_USER_MODEL = "useraccount.User"

SITE_ID = 1 

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

SIMPLE_JWT = {
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "kuchbibadmaidekhygy",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS":  False,
     "UPDATE_LAST_LOGIN": True,
     "BLACKLIST_AFTER_ROTATION":False,
     
    
    
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = None

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:3000',
    "https://arifbnb.netlify.app",
    "http://airbnbbackend-production.up.railway.app",
    
]
CSRF_TRUSTED_ORIGINS = [
    'https://airbnbbackend-production.up.railway.app',
   # 'https://your-other-domain.com'  # Include other domains if necessary
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:3000',
    "https://arifbnb.netlify.app"
]



CORS_ALLOW_ALL_ORIGINS = True

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False
}



# Application definition

INSTALLED_APPS = [
    'daphne',
    "channels",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'allauth',
    'allauth.account',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'corsheaders',

    'chat',
    'property',
    'useraccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

#WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': os.environ.get("SQL_ENGINE"),
            
            'NAME': os.environ.get("SQL_DATABASE"),
            
            'USER': os.environ.get("SQL_USER"),
            
            'PASSWORD': os.environ.get("SQL_PASSWORD"),
            
            'HOST': os.environ.get("SQL_HOST"),
            
            'PORT': os.environ.get("SQL_PORT"),
            
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/re/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL  = "media/"
MEDIA_ROOT = BASE_DIR/ "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
