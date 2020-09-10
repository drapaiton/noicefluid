from channels.generic.websocket import AsyncWebsocketConsumer
from chat.datastructures import JsonMsgDict
import json
from . import datastructures
from . import tasks

COMMANDS = {
    # use lowercase
    'addvideo': {
        'help': 'adds to the queue a youtube link video',
        'task': 'addvideo'
    },
    'queryvideo': {
        'help': 'search by keywords with the youtube api',
        'task': 'queryvideo'
    }
}


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "uno"

        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data: str):
        text_data_json = json.loads(text_data)
        try:
            message = JsonMsgDict(**text_data_json)

            if message.type == 'command_message':
                # send task
                getattr(tasks, COMMANDS[message.task]['task']).delay(
                    self.channel_name, content=message.content)

            await self.channel_layer.group_send(
                self.room_group_name, message)

        except Exception as i:
            print(i)

    async def chat_message(self, event):
        print(event, type(event))
        await self.send(text_data=json.dumps({
            'message': 'omg'
        }))
