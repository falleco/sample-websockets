from datetime import datetime
import time

from bottle import route, run, view


@route('/long')
@view('long_polling')
def long_view():
    return dict(name="Israel")


@route('/api/long-poll')
def long_poll():
    # Wait until we have data, and then release our connection
    while datetime.now().second % 5 != 0:
        time.sleep(1)

    # Just wait another second
    print "Long polling at {}".format(datetime.now())
    time.sleep(1)

    return {"beat": True}


@route('/ajax')
@view('ajax_request')
def ajax_view():
    return dict(name="Israel")


@route('/api/poll')
def poll():
    # Just answer with our information as faster as possible and
    # get ready to the next request
    return {"beat": datetime.now().second % 5 == 0}

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)