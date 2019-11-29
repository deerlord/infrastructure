import speech_recognition as sr
import stanfordnlp
#import intent_engine
#from nltk.tag import StanfordNERTagger
#from nltk.tokenize import word_tokenize

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
    keyword, *command = text.split(' ')
    if keyword.lower() != KEYWORD:
        return None
    doc = NLP(' '.join(command))
    return doc


def __parse_intent(sentences):
    pass


def pipeline(audio):
    data = {'keyword': '', 'verbs': []}
    text = __parse_audio(audio)
    if len(text) == 0:
        return None  # no actual text
    doc = __parse_text(text)
    if doc:
        intent = __parse_intent(doc.sentences)
    return data
