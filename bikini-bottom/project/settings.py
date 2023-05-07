import os
from pathlib import Path
from project import secret

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = secret.secure['key']
DEBUG = secret.secure['debug']
ALLOWED_HOSTS = secret.secure['host']

# APPS DEFINITION
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # Crispy forms
    'crispy_forms',
    'crispy_bootstrap5',

    # Leaflet
    'leaflet',

    # Custom Apps
    'accounts',
    'tourism',
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

ROOT_URLCONF = 'project.urls'
LOGIN_REDIRECT_URL = '/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'assets/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom Context Processor
                'project.context_processors.profile',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# DATABASE
DATABASES = {
    'default': secret.db_default
}


# PASSWORD VALIDATION
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


# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# STATIC FILES
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets/static')
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets/static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/media')

# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# GDAL using wheel downloads
if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(
        VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(
        VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']
    
# LEAFLET CONFIGURATION
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': [11.60, 165.39],
    'DEFAULT_ZOOM': 11,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'SCALE' : 'metric',
    'RESET_VIEW': False,
    'ATTRIBUTION_PREFIX' : 'Bikini Bottom City Council | Leaflet',

    'TILES': [
        ('OpenStreetMap', 'https://tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': ' © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}),
        ('ESRI Imagery', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': '© <a href="https://www.arcgis.com/">Esri</a>, Maxar, Earthstar Geographics, and the GIS User Community'})
    ],
}

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"