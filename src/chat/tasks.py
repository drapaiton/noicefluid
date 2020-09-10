# django
from chat.datastructures import JsonMsgDict
from typing import List
from celery import shared_task
from asgiref.sync import async_to_sync
from django.core.cache import cache
from channels.layers import get_channel_layer
# youtube
from django.apps import apps
# py
from typing import List
from . import datastructures
channel_layer = get_channel_layer()


@shared_task
def addvideo(channel_name: str, id: str) -> None:
    pass


@shared_task
def queryvideo(channel_name: str, content: str) -> List[str]:
    max_results = 10

    youtube = apps.get_app_config('chat').YOUTUBE_API
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=content,
        part="id,snippet",
        maxResults=max_results
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result["id"]["videoId"])

    output = JsonMsgDict(
        type='bot_message', content="\n".join(videos), author="noiceBot")

    async_to_sync(channel_layer.send)(
        channel_name, output)
