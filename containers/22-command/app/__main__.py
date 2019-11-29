from http.server import BaseHTTPRequestHandler, HTTPServer
import aiohttp
from io import BytesIO
import openhab
import language

KEYWORD = 'hal'

class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        command = language.pipeline(audio)
        # find what openhab function we need to run
        # ex:
        #    # parse command to item, cmd
        #    openhab.use_item(item, cmd)
        self.send_response(200 if result else 500)
        self.end_headers()
        response = BytesIO()
        self.wfile.write(response)


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()

