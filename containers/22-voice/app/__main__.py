from http.server import BaseHTTPRequestHandler, HTTPServer
import language
import intent

KEYWORD = 'hal'
k_len = len(KEYWORD.split(' ')


def __keyword_check(sentence):
    return (
        True
        if ' '.join(sentence[k_len]).lower() == KEYWORD
        else False
    )


def process(audio_data):
    nlp_result = language.pipeline(audio_data)
    request = intent.pipeline(nlp_request)
    return True


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        result = process(audio)
        self.wfile.write(bytes(result, 'ascii')) # not sure if right


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()

