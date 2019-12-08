from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import openhabapi
import language

KEYWORD = 'HAL'.lower()

class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        retval = False
        result = language.pipeline(audio)
        # convert into command
        """
        command = {
            'action': 'on',
            'group': None,
            'item': 'all',

        }
        """
        if result:
            print(result)
            #openhab.request(command)
            retval = True
        #self.send_response(200 if retval else 500)
        #self.end_headers()
        self.wfile.write(b'')


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()
