import os
from .common import *
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['adebuy-prod.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}