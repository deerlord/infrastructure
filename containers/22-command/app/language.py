import speech_recognition as sr
import stanfordnlp
from openhabapi import ACTIONS

NLP = stanfordnlp.Pipeline(lang='en')
KEYWORD = 'hal'

def __parse_audio(audio):
    result = None
    try:
        r = sr.Recognizer()
        print('writing audio file')
        with open('audio', 'wb') as f:
            f.write(audio)
        print('reading audio file')
        with sr.AudioFile('audio') as source:
            audio = r.record(source)
        result = r.recognize_sphinx(audio)
        print('got result')
        print(result)
    except Exception as e:
        print(e)
    """
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    except:
        pass
    """
    return result


def __simple_intent(words):
    data = {
        'action': None,
        'item': None,
        'group': None,
    }

    if words[0].lower() == 'turn':
        if words[1] == 'off':
            data['action'] = 'off'
        elif words[1] == 'on':
            data['action'] = 'on'
        item = data[2:]
    elif words[0].lower() == 'play':
        data['action'] = 'play'
        item = data[1:]
    elif words[-1].lower() == 'leaving':
        data['action'] = 'off'
        data['group'] = 'idle'
        data['item'] = 'all'
        # idle house setting
    elif words[-1].lower() == 'home':
        data['action'] = 'on'
        data['group'] = 'idle'
        data['item'] = 'all'
        # house active


def __keyword_check(keyword):
    return keyword.lower() == KEYWORD


def __parse_text_simple(text):
    return text.split(' ')


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
    if not text:
        return None
    if len(text) == 0:
        return None  # no actual text
    words = __parse_text_simple(text)
    if len(words) > 0:
        if __keyword_check(words[0]):
            intent = __simple_intent(words[1:])
    return data
