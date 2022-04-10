import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@shared_task
def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url).json()
    joke = response['value']['joke']

    async_to_sync(channel_layer.group_send)('jokes', {'type': 'send_jokes', 'text': joke})
