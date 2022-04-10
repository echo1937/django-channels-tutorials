from django.urls import path

from graph.consumers import GraphConsumer
from integers.consumers import WSConsumer
# from jokes.consumers import JokesConsumer

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi()),
    path('ws/graph/', GraphConsumer.as_asgi()),
    # path('ws/jokes/', JokesConsumer.as_asgi()),
]

