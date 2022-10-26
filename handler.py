from http.server import BaseHTTPRequestHandler

class JsonPostHandler(BaseHTTPRequestHandler) :
  def do_POST(self):
      self.send_responce