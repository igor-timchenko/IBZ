# chat/routing.py

from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:chat_name>/', ChatConsumer.as_asgi()),
]
