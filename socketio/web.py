# import sys
# sys.path.insert(0, "lib/gevent-0.13.8")
# sys.path.insert(0, "lib/bottle")
# sys.path.insert(0, "lib/gevent-socketio")

from gevent import monkey
monkey.patch_all()

#
from socketio import socketio_manage, mixins
from socketio.namespace import BaseNamespace
from bottle import route, run, view, request, static_file


class HeartBeatNamespace(BaseNamespace, mixins.BroadcastMixin):
    def on_beat(self, msg):
        print "On beat!"
        self.broadcast_event("pulse", "")


@route('/')
@view("index")
def index():
    return {}

@route("/static/<file:path>")
def static(file):
    return static_file(file, root="static")


@route('/socket.io/<remaining:path>')
def socketio_service(remaining):
    context = {'/beat': HeartBeatNamespace}
    socketio_manage(request.environ, context, request)

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True, server="geventSocketIO", resource="socket.io")