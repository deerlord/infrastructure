from http.server import BaseHTTPRequestHandler, HTTPServer
import audio
import intent

print("begin http server prep")


KEYWORD = 'hal'
k_len = len(KEYWORD.split(' '))

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
    text = audio.process(data)
    try:
        keywords = ' '.join(text.split(' ')[k_len])
    except:
        pass  # k_len not a valid length
    if keywords != KEYWORD:
        return
    return intent.process(text)


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("entering POST handler")
        content_length = int(self.headers['Content-Length'])
        pritn("content length is: ", content_length)
        audio = self.rfile.read(content_length)
        print("read audio file, sending 200")
        self.send_response(200)
        print("sent response")
        self.end_headers()
        print("ended headers, processing audio")
        action = process(audio)

print("creating http server")
httpd = HTTPServer(('', 8080), SpeechHandler)
print("starting server")
httpd.serve_forever()

