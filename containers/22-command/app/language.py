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
            if 'Number' in next_word.feats

def pipeline(audio):
    data = {'keyword': '', 'verbs': []}
    text = __parse_audio(audio)
    if len(text) == 0:
        return None  # no actual text
    doc = __parse_text(text)
    if doc:
        intent = __parse_intent(doc.sentences[0].words)
    return data
