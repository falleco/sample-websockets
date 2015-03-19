from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace
from socketio.mixins import BroadcastMixin


@namespace('/beat')
class EchoNamespace(BaseNamespace, BroadcastMixin):
    def on_beat(self, msg):
        print "On beat!"
        self.broadcast_event("pulse", "")

    def on_join(self, msg):
        print "Hello, sir!"
        self.broadcast_event("join", "")