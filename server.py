from http.server import HTTPServer
import socketserver
import json
import string

class HTTPLocalWebServer:
    def __init__(self, port= 8080):
      self._PORT = port
      self._ADDRESS = ('localhost', port)

    def get_address(self):
      return self._ADDRESS

    def listen_post(self, RequestHandlerClass):
      with HTTPServer(self._ADDRESS, RequestHandlerClass) as server:
        print("serving at:", self._ADDRESS)
        server.serve_forever()