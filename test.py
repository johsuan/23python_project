import sys

import http.server

from http.server import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler

ServerClass  = http.server.HTTPServer

Protocol     = "HTTP/1.0"


if sys.argv[1:]:

    port = int(sys.argv[1])

else:

    port = 8080

server_address = ('0.0.0.0', port)


HandlerClass.protocol_version = Protocol

httpd = ServerClass(server_address, HandlerClass)


sa = httpd.socket.getsockname()

print("Serving HTTP on", sa[0], "port", sa[1], "...")

httpd.serve_forever()



