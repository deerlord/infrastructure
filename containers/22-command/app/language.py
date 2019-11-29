import speech_recognition as sr
import stanfordnlp

KEYWORD='hal'

def parse_audio(audio):
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


def parse_text(text):
    nlp = standfordnlp.Pipeline()
    doc = nlp(text)
    # probably need to parse this further, such as returning
    # noun (item), command (verb), etc.
    return doc

def parse_language(data):
    return data


def pipeline(audio):
    text = parse_audio(audio)
    if len(text) == 0:
        return None  # no actual text
    language = parse_text(text)
    # depending on how this is parsed in language_text(),
    # may need to parse further. 
    result = parse_langauge(language)
    return result
