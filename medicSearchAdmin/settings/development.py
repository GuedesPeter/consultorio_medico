
from .settings import *


DEBUG = True

SECRET_KEY = 'django-insecure--e!q6qi^3kats#r$aspcqp!7&sx2kfx#%%34k(rlr))8mjsd4*'

# VARIÁVEL QUE CONFIGURA IP INDIVIDUAL POR AMBIENTE
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}