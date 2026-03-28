"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url # <--- IMPORTANTE: Adicionamos essa biblioteca para o banco real

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x9k8^lkmkaom**76(ae@1i@!2#1vwxuw*aum6n3d*32vb)q-px'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# No deploy, permitimos o endereço que o Render vai nos dar
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mostra',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ESSENCIAL PARA O DEPLOY
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# --- BANCO DE DADOS (CONFIGURAÇÃO HÍBRIDA) ---
# Ele busca a variável DATABASE_URL no Render. Se não achar, usa o SQLite.
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- ARQUIVOS ESTÁTICOS E MÍDIA ---

STATIC_URL = 'static/'

# Pasta onde o Django vai reunir tudo no servidor para o deploy
STATIC_ROOT = BASE_DIR / "staticfiles"

# Onde o Django busca seus arquivos de desenvolvimento
STATICFILES_DIRS = [
    BASE_DIR / "mostra" / "static",
]

# Modo mais tolerante do WhiteNoise para não dar erro no build
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Configuração de Media (Imagens e PDFs que você sobe no Admin)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'