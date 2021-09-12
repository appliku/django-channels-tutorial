from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from mychat.consumers import MyConsumer

websocket_urlpatterns = [
    path(r'chat', MyConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
})