import dj_database_url
from decouple import config
from .settings import DATABASES

CELERY_BROKER_URL = config('REDIS_URL')
CELERY_RESULT_BACKEND = config('REDIS_URL')

SECRET_KEY = config('SECRET_KEY')

DATABASES['default'].update(dj_database_url.config(
    conn_max_age=500, ssl_require=True))

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": config('REDIS_URL'),
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

appliedProductionSettings = True
