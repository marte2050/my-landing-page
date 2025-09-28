import sys
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$5@jr4y_%b@+mn5d5=iaz^%ht6yxp1lcm5vnxsvhv-#m2zp#0m"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

TESTING = 'pytest' in sys.argv[0] or any('pytest' in arg for arg in sys.argv)

if TESTING:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }

try:
    from .local import *
except ImportError:
    pass
