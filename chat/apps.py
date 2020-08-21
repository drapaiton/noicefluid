# Html Get
from apiclient.discovery import build
from decouple import config
# django
from django.apps import AppConfig

# Trash After YOUTUBE_API Creation
DEVELOPER_KEY = config("YOUTUBE_TOKEN")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class chatConfig(AppConfig):  # Our app config class
    name = "chat"
    YOUTUBE_API = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)
