import os
import dj_database_url
from django.utils import crypto

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', crypto.get_random_string(60))
DEBUG = 'DEBUG' in os.environ
ALLOWED_HOSTS = ['*']
DATABASES = {'default': dj_database_url.config(default='postgres:///bugbounty')}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'floppyforms',
    'social.apps.django_app.default',
    'bugbounty',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bugbounty.urls'

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
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'bugbounty.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files: use vendored in USWDS, and Whitenoise for serving.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "third-party/uswds-0.9.1")
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Slack for notifications
SLACK_INCOMING_WEBHOOK = os.environ.get('SLACK_INCOMING_WEBHOOK', None)

# python-social-auth config - use github
AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubTeamOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GITHUB_TEAM_KEY = os.environ.get('GITHUB_KEY', None)
SOCIAL_AUTH_GITHUB_TEAM_SECRET = os.environ.get('GITHUB_SECRET', None)

# The team ID doesn't seem to be easy to find on the web anywhere, so I
# ended up using the API to find it. Using github3.py, I did this::
#       gh = github3.login(...)
#       next(t for t in gh.organization('18f').teams() if t.name == '18F').id
SOCIAL_AUTH_GITHUB_TEAM_ID = os.environ.get('GITHUB_TEAM_ID', None)

# This isn't documented, but GithubTeamOAuth2 needs the read:org permission
# to be able to tell if you're in the given team.
SOCIAL_AUTH_GITHUB_TEAM_SCOPE = ['read:org']
