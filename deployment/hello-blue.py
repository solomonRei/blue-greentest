from wsgiref.simple_server import make_server

GREETING = b'Hello, BLUE world!\n'

def hello(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [GREETING]

make_server('0.0.0.0', 80, hello).serve_forever()
