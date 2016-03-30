from settings import *

DEBUG = True
CITY_DATABASE = 'city_data.db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, CITY_DATABASE),
    }
}