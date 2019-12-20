from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import openhabapi
import language


STREAMABLE = [
    'play',
]


def stream_chunk(client, chunk):
    return client.wfile.write('{}\r\n{}\r\n'.format(len(chunk), chunk))


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        retval = False
        data = language.pipeline(audio)
        if data['error']:
            print('result it')
            print(result)
        else:
            result = openhab.request(data)
        # check result
        if data['verb'] in STREAMABLE:
            for chunk in result.stream():
                size = hex(len(chunk))[2:]
                packet = '{}\r\n{}\r\n'.format(size, chunk)
                self.wfile.write(packet)
            self.wfile.write('0\r\n\r\n')
        else:
            self.wfile.write(bytes(result, 'ascii')) # not sure if right


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()
