import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('HEROKU_POSTGRESQL_WHITE_URL')
    )
}
