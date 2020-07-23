import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('HEROKU_POSTGRESQL_WHITE_URL')
    )
}

# temp files fix (?)
# STATIC_TMP = os.path.join(BASE_DIR, 'static')
# os.makedirs(STATIC_TMP, exist_ok=True)
