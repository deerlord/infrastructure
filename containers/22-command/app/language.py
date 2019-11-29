import speech_recognition as sr
import stanfordnlp

NLP = stanfordnlp.Pipeline(lang='en')

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
    retval = ''
    doc = NLP(text)
    if len(sentences) > 1:
        s = sentences[0]
        if len(s.words) >= 2:
            retval = s
    return retval

def parse_language(sentence):
    keyword = sentence.words[0].text
    verbs = [
        for word in sentence.words[1:]
        if word.upos == 'VERB'
    ]
    return keyword, verbs


def pipeline(audio):
    keyword = ''
    verbs = []
    text = parse_audio(audio)
    if len(text) == 0:
        return None  # no actual text
    doc = parse_text(text)
    if doc != '':
      keyword, verbs = parse_language(doc)
    return keyword, verbs
