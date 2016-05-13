import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bugbounty.settings")
application = get_wsgi_application()

# Throw the whole site behind basic auth, if requested. This is temporary
# until the site gets ATO'd.
if 'WSGI_AUTH_CREDENTIALS' in os.environ:
    import wsgi_basic_auth
    application = wsgi_basic_auth.BasicAuth(application)