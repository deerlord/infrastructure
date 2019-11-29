from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from openhab import OpenHAB
import language

KEYWORD = 'HAL'.lower()
base_url = 'http://openhab:8080/rest'
hab = OpenHAB(base_url)


def openhab_process(command):
    """
    # figure out wtf we are doing
    if interact with item
      items = hab.()
      i = items.get(item_name)
      if i
       # might need to parse
       i.command(cmd)
    """
    pass


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        retval = False
        result = language.pipeline(audio)
        if result:
            openhab_process(command)
            retval = True
        self.send_response(200 if retval else 500)
        self.end_headers()
        response = BytesIO()
        self.wfile.write(response)


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()
