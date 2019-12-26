from http.server import BaseHTTPRequestHandler, HTTPServer
import audio
import language
import intent

KEYWORD = 'hal'
k_len = len(KEYWORD.split(' ')

def process(data):
    """
    Glue function for processing intent from audio.

    Passed audio to language.process() to convert to text. Then uses
    intent.process() to handle converting this text to a meaningful request.

    Parameters:
    audio_data (binary .wav data)

    Returns:
    list: list of processed word objects.
    """
    text = audio.process(audio_data)
    words = language.process(text)
    sentence = result.sentence[0]
    return (
        intent.process(sentence)
        if ' '.join(sentence[k_len]).lower() == KEYWORD
        else ''
    )


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        process(audio)



httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()

