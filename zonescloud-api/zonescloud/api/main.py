import webapp2
from zonescloud.util import webutil

class PingHandler(webutil.RequestHandler):
    def get(self):
        self.send_json("OK")

app = webapp2.WSGIApplication([
    ('/api/ping', PingHandler)
])
