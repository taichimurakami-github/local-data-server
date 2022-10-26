import http.server
import socketserver
import json

class LocalWebServer:
    def __init__(self, port= 8080):
      self._PORT = port
      self._Handler = http.server.BaseHTTPRequestHandler


    def listen_post(self):
      PORT = self._PORT
      Handler = self._Handler
      with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port:", PORT)
        httpd.serve_forever()