import httplib
import urllib
import urlparse
from jsonutil import JSON

class Error(Exception):
    """Exceptions"""

def close(obj):
    try:
        obj.close()
    except:
        """ Done """

class Response(object):
    def __init__(self, req, status, headers, body):
        self.req = req
        self.status = status
        self.raw_headers = headers
        self.body = body
        self.headers = dict(headers)

    def body_json(self):
        return JSON.parse(self.body) if self.body else None

    def body_form_array(self):
        return urlparse.parse_qs(self.body)

    def body_form(self):
        return dict(urlparse.parse_qsl(self.body))

    def body_text(self):
        return self.body

class Request(object):
    def __init__(self, method, url):
        self.method = method
        self.url = url
        self.headers = {
            'User-Agent': [ 'tiny-ci' ]
        }
        self._payload = None

    def add_header(self, name, value, op = False):
        values = self.headers.get(name)
        if values and op:
            return self
        if not values:
            values = []
            self.headers[name] = values
        values += [value]
        return self

    def send_json(self, payload):
        self.add_header('Content-Type', 'application/json; charset=UTF-8', True)
        self._payload = JSON.stringify(payload or {})
        return self

    def send_form(self, payload):
        self.add_header('Content-Type', 'application/x-www-form-urlencoded', True)
        self._payload = urllib.urlencode(payload or {})
        return self

    def execute(self, expects = [200]):
        print 'Req: %s %s' % (self.method, self.url[:100])
        self.add_header('User-Agent', 'tiny-ci', True)
        parsed = urlparse.urlparse(self.url)
        host = parsed.netloc
        uri = parsed.path
        if(parsed.query != ''):
            uri = uri + '?' + parsed.query
        conn = None
        if(parsed.scheme == 'https'):
            conn = httplib.HTTPSConnection(parsed.hostname, parsed.port or 443)
        else:
            conn = httplib.HTTPConnection(parsed.hostname, parsed.port or 80)
        try:
            conn.putrequest(self.method, uri, skip_accept_encoding=True)
            if self._payload != None:
                self.add_header('Content-Length', len(self._payload), True)
            for key, values in self.headers.iteritems():
                for value in values:
                    conn.putheader(key, value)
            conn.endheaders(self._payload)
            resp = conn.getresponse()
            body = resp.read()
            print 'Resp: %s %s' % (resp.status, resp.reason)
            if resp.status not in expects:
                raise Error('Status: %d %s %sri' % (resp.status, resp.reason, body))
            return Response(self, resp.status, resp.getheaders(), body)
        finally:
            close(conn)


def __main():
    req = Request('GET', 'https://api.github.com/meta')
    #req = Request('GET', 'http://localhost:5000/abc')
    resp = req.execute()
    print resp
    print dir(resp)
    print resp.status
    print resp.raw_headers
    print resp.headers['content-type']
    print resp.body_json()

if __name__ == '__main__':
    __main()
