"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url # Biblioteca para o banco real no Render

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x9k8^lkmkaom**76(ae@1i@!2#1vwxuw*aum6n3d*32vb)q-px'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Permitimos o endereço que o Render vai nos dar
ALLOWED_HOSTS = ['*']

# ==============================================================================
# 1. APPS INSTALADOS 
# ==============================================================================
INSTALLED_APPS = [
    'jazzmin',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mostra', # seu app
]

# ==============================================================================
# 2. MIDDLEWARE (Configurado para Deploy/WhiteNoise)
# ==============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
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

# ==============================================================================
# 3. BANCO DE DADOS (Configuração Híbrida para Deploy)
# ==============================================================================
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}

# Validação de Senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internacionalização (Brasil)
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# 4. ARQUIVOS ESTÁTICOS E MÍDIA
# ==============================================================================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "mostra" / "static",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================================================================
# 5. CONFIGURAÇÃO JAZZMIN 
# ==============================================================================
JAZZMIN_SETTINGS = {
    "site_title": "Portal de Gestão - Mostra UFJ",
    "site_header": "Mostra UFJ",
    "site_brand": "Computação - UFJ",
    
  
    "site_logo": "mostra/img/logo_ufj_branca.png", 
    "login_logo": "mostra/img/logo_ufj_branca.png", 
    
    "site_icon": "mostra/img/logo_ufj_branca.png",
    "welcome_sign": "Bem-vindo ao Portal de Gestão da Mostra UFJ",
    "copyright": "UFJ - Ciência da Computação © 2026",
    
    "user_avatar": None,
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "mostra.Projeto": "fas fa-project-diagram",
        "mostra.Pesquisa": "fas fa-flask",
    },
}

# Ajustes de Cores para forçar o AZUL e estilo moderno
JAZZMIN_UI_TWEAKS = {
    "navbar_variant": "navbar-dark",
    "theme": "flatly",        # Tema azul profissional
    "dark_mode_theme": None,
    "navbar": "navbar-primary",
    "brand_variant": "navbar-primary",
    "accent": "accent-primary",
}