import speech_recognition as sr
import stanfordnlp
from openhabapi import ACTIONS

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


def __simple_intent(text):
    _text = text
    text = text.lower()
    words = text.split(' ')
    data = {
        'action': None,
        'item': None,
    }
    if words[0] == 'turn':
        if words[1] == 'off':
            data['action'] = 'off'
        elif words[1] == 'on':
            data['action'] = 'on'
        item = ' '.join(data[2:])
    elif words[0] == 'play':
        data['action'] = 'play'
        item = ' '.join(data[1:])
    if words[-1] == 'leaving':
        data['action'] = 'off'
        data['action'] = 'home'
        # idle house setting
    elif words[-1] == 'home':
        data['action'] = 'on'
        data['item'] = 'home'
        # house active


def __parse_text_simple(text):
    return text


def __parse_text(text):
    retval = ''
    keyword, *command = text.split(' ')
    if keyword.lower() != KEYWORD:
        return None
    doc = NLP(' '.join(command))
    return doc

def __parse_verbs(words):
    return [
        word
        for word in words
        if word.upos == 'VERB'
    ]

def __parse_nouns(words, index):
    return [
        word
        for word in words
        if word.upos == 'NOUN'
    ]


def __find_object(nouns):
    data = {
        'multiple': False,
        'object': None,
    }
    for noun in nouns:
        if noun.dependency_relation == 'obj':
            if 'Number' in noun.feats and 'Plur' in noun.feats:
                data['multiple'] = True
            data['object'] = noun.text
            break
    return data

def __parse_complex_noun(words, index):
    initial = words[index]
    if initial.type != 'NOUN':
        return
    if initial.dependency_relation == 'compound':
        next_word = words[index + 1]
        if next_word.dependency_relation == 'obj':
            if 'Number' in next_word.feats:
                pass  # not sure what I was doing

def pipeline(audio):
    data = {'keyword': '', 'verbs': []}
    text = __parse_audio(audio)
    if len(text) == 0:
        return None  # no actual text
    doc = __parse_text_simple(text)
    if doc:
        intent = __simple_intent(doc.sentences[0].words)
    return data
