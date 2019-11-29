import speech_recognition as sr
import stanfordnlp

NLP = stanfordnlp.Pipeline(lang='en')

def __parse_audio(audio):
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


def __parse_text(text):
    retval = ''
    doc = NLP(text)
    if len(sentences) > 1:
        s = sentences[0]
        if len(s.words) >= 2:
            retval = s
    return retval

def __parse_language(sentence):
    keyword = sentence.words[0].text.lower()
    verbs = [
        for word in sentence.words[1:]
        if word.upos == 'VERB'
    ]
    return keyword, verbs


def pipeline(audio):
    data = {'keyword': '', 'verbs': []}
    text = __parse_audio(audio)
    if len(text) == 0:
        return None  # no actual text
    doc = __parse_text(text)
    if doc != '':
      keyword, verbs = __parse_language(doc)
      data.update({'keyword': keyword, 'verbs': verbs})
    return data
