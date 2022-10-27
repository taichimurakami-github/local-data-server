from datetime import datetime
import os
from server import HTTPLocalWebServer
from handler import JsonPostHandler

if __name__ == '__main__':
  server = HTTPLocalWebServer(8888)
  server.listen_post(JsonPostHandler)