from http.server import BaseHTTPRequestHandler, HTTPServer
import aiohttp
from io import BytesIO
import speech_recognition as sr

KEYWORD='hal'

def speech_to_text(audio):
    result = None
    try:
        r = sr.Recognizer()
        result = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    except:
        pass
    return result


def execute_command(cmd):
    pass


def process(audio):
    retval = False
    text = speech_to_text(audio)
    if isinstance(text, str) and len(str):
        words = text.split(' ')
        if not isinstance(words, list):
            return retval
        keyword = words.pop().lower()
        if not len(words):
            return retval
        cmd = ' '.join(words)
    else:
        keyword = ''
    return execute_command(cmd) if keyword == KEYWORD else None


class SpeechHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        audio = self.rfile.read(content_length)
        result = process(audio)
        self.send_response(200 if result else 500)
        self.end_headers()
        response = BytesIO()
        self.wfile.write(response)


httpd = HTTPServer(('', 8080), SpeechHandler)
httpd.serve_forever()

