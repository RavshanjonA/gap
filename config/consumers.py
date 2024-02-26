import json

from channels.generic.websocket import AsyncWebsocketConsumer


class OpinionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connection created")
        self.opinion_pk = self.scope["url_route"]['kwargs']['pk']
        self.room_group_name = "chat_%s" % self.opinion_pk
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.channel_layer,
            self.room_group_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        room = data["room"]
        await  self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room
            }
        )
        await self.save_message(message=message, username=username, room=room)

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room
        }))
