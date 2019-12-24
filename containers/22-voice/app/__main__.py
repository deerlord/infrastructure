from http.server import BaseHTTPRequestHandler, HTTPServer
import language
import intent

KEYWORD = 'hal'
k_len = len(KEYWORD.split(' ')


def process(audio_data):
    result = language.pipeline(audio_data)
    # need to do some checking here
    sentence = result.sentence[0]
    return (
        intent.pipeline(sentence)
        if ' '.join(sentence[k_len]).lower() == KEYWORD
        else ''
    )


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        result = process(audio)
        if result:
            pass  # handle, maybe command to openhab?


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()

