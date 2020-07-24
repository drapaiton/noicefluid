import dj_database_url
from decouple import config
from .settings import DATABASES

DATABASES['default'].update(dj_database_url.config(
    conn_max_age=500, ssl_require=True))
