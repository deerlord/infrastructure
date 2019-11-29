from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import openhab
import language

KEYWORD = 'HAL'.lower()

class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        retval = False
        result = language.pipeline(audio)
        if result['keyword'] == KEYWORD:
            pass  # do the things
            # ex: openhab.use_item(item, cmd)
            # retval = True
        self.send_response(200 if retval else 500)
        self.end_headers()
        response = BytesIO()
        self.wfile.write(response)


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()
