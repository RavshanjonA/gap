from django.urls import path

from config.consumers import OpinionConsumer

websocket_urlpatterns = [
    path('ws/gap/room/<int:pk>/', OpinionConsumer.as_asgi())
]