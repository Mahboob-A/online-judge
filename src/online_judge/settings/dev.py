from .base import *  # noqa
from .base import env  # noqa: E501


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DEV_DJANGO_SECRET_KEY",
    default="django-insecure-7s1m)m)#ogw5qcv3yq=wl9-k%#ggd@-470b!=^$h-e-62ul3)k",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")
if DEBUG == "True":
    DEBUG = True
else:
    DEBUG = False

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]

ALLOWED_HOSTS = ["127.0.0.1"]
