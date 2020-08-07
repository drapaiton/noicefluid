from asgiref.sync import async_to_sync
from . import tasks

# important
import json
from channels.generic.websocket import WebsocketConsumer

# USE LOWERCASE
COMMANDS = {
    'help': {
        'help': 'Display help message.',
    },
    'sum': {
        'args': 2,
        'help': 'Calculate sum of two integer arguments. Example: `sum 12 32`.',
        'task': 'sum'
    },
    'add': {
        'args': 1,
        'help': 'adds to the queue a youtube link video',
        'task': 'add'
    }

}


class ChatConsumer(WebsocketConsumer):

    # TODO protocols

    # def connect(self):
    #     self.accept()

    # def disconnect(self, close_code):
    #     pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        response_message = 'youtube title name not valid'
        message_parts = message.split()

        if message_parts:
            command = message_parts[0].lower()
            if command == 'help':
                response_message = 'List of the available commands:\n' + \
                    '\n'.join(
                        [f'{command} - {params["help"]} ' for command, params in COMMANDS.items()])
            elif command in COMMANDS:
                if command == 'add':
                    # join all parameters into a string
                    message_parts[1:] = [' '.join(message_parts[1:])]
                if len(message_parts[1:]) != COMMANDS[command]['args']:
                    response_message = f'Wrong arguments for the command `{command}`.'
                else:
                    getattr(tasks, COMMANDS[command]['task']).delay(
                        self.channel_name, *message_parts[1:])
                    response_message = f'Command `{command}` received.'

        async_to_sync(self.channel_layer.send)(
            self.channel_name,
            {
                'type': 'chat_message',
                'message': response_message
            }
        )

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': f'[bot]: {message}'
        }))
