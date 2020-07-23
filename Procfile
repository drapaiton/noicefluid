web: daphne noicefluid.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: REMAP_SIGTERM=SIGQUIT celery worker --app noicefluid.celery.app --loglevel info