from datetime import datetime
from http.server import BaseHTTPRequestHandler
import json
import os
from urllib.parse import parse_qs, urlparse
from multiprocessing import Process

def write_json_file(dataStr, filename):
  dirpath = os.path.join(os.getcwd(), 'data', '{}'.format(datetime.now().date()))

  if os.path.exists(dirpath) == False:
    print(f"creating new dirpath '{dirpath}'")
    os.makedirs(dirpath)

  filepath = os.path.join(dirpath, filename)

  with open(filepath, 'w') as f:
    print(f"creating new file at '{filepath}'")
    f.write(dataStr)

class JsonPostHandler(BaseHTTPRequestHandler) :

  _FILE_WRITE_DIR_PATH = os.path.join(os.getcwd(), 'data', '{}'.format(datetime.now().date()))

  # Private methods
  def _print_request_info(self):
    print('############ INFO ############')
    print(f'write path: {self._FILE_WRITE_DIR_PATH}')
    print('headers\r\n-----\r\n{}-----'.format(self.headers))
    print('body = {}'.format(self._get_body_content_str()))

    parsed_path = urlparse(self.path)
    print('path = {}'.format(parsed_path))
    print('parsed query = {}'.format(parse_qs(parsed_path.query)))


  def _get_parsed_queries(self):
    parsed_path = urlparse(self.path)
    parsed_queries = parse_qs(parsed_path.query)
    return parsed_queries


  def _get_body_content_str(self):
    content_length = int(self.headers['content-length'])
    return self.rfile.read(content_length).decode('utf-8')


  def _write_json_from_text(self, dataStr, filename: str):
    dirpath = self._FILE_WRITE_DIR_PATH

    if os.path.exists(dirpath) == False:
      print(f"creating new dirpath '{dirpath}'")
      os.makedirs(dirpath)

    filepath = os.path.join(dirpath, filename)

    with open(filepath, 'w') as f:
      print(f"creating new file at '{filepath}'")
      f.write(dataStr)

  def _send_ok_res(self):
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain; charset=utf-8')
    self.end_headers()

  def _send_error_res(self, bodyMessage: str):
    self.send_response(400)
    self.send_header('Content-Type', 'text/plain; charset=utf-8')
    self.end_headers()
    self.wfile.write(bodyMessage.encode())

  # Public methods
  def do_POST(self):
    # self._print_request_info()

    # parse query
    queries = self._get_parsed_queries()

    if(queries.keys().__contains__('filename') == False):
      self._send_error_res("E_INVALID_QUERY_PARAMETERS")
      return

    filename = queries['filename'][0]

    # get body content and write json file
    bodyContent = self._get_body_content_str()
    parsedBodyContent = bodyContent.replace('\n', '')
    self._write_json_from_text(parsedBodyContent, filename)

    # send response
    self._send_ok_res()