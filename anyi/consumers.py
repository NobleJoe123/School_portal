# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "test_scores"  # You can make this dynamic if needed
        self.room_group_name = f"test_scores"

        # Join the WebSocket group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the WebSocket group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket (scores from test page)
    async def receive(self, text_data):
        data = json.loads(text_data)

        student_id = data['student_id']
        ca_score = data['ca_score']
        # Add the test score into the exam page (update real-time)

        # Broadcast the test score to the exam page
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'update_exam_scores',
                'student_id': student_id,
                'ca_score': ca_score,
            }
        )

    # Receive message from the group (when test score is updated)
    async def update_exam_scores(self, event):
        student_id = event['student_id']
        ca_score = event['ca_score']

        # Send the updated score to the WebSocket
        await self.send(text_data=json.dumps({
            'student_id': student_id,
            'ca_score': ca_score,
        }))
