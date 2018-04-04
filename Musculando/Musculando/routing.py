from channels import route
from apps.Panel import consumers
from apps.Panel.consumers import debug

channel_routing = [
 # Las funciones se definen en consumers.py
 route("websocket.connect", consumers.ws_connect),
 route("websocket.receive", consumers.ws_receive),
 route('debug',consumers.debug),
]