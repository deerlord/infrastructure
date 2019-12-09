from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import openhabapi
import language


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
        if data['command'] == 'play':
            for chunk in result:
                client.wfile.write(
                    '{}\r\n{}\r\n'.format(
                        hex(len(chunk)),
                        chunk
                    )
                )
            client.wfile.write('0\r\n\r\n')
        #self.send_response(200 if retval else 500)
        #self.end_headers()
        self.wfile.write(b'')


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()
