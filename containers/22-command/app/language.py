from io import BytesIO
import speech_recognition as sr
import stanfordnlp

NLP = stanfordnlp.Pipeline(lang='en')
KEYWORD = 'Hal'
R = sr.Recognizer()
R.dynamic_energy_threshold = True

def __parse_audio(audio):
    result = None
    try:
        sample_rate = int.from_bytes(
            audio[24:28],
            byteorder='little',
        )
        sample_width = 2
        b_audio = audio[44:]
        s_audio = sr.AudioData(
            b_audio,
            sample_rate=sample_rate,
            sample_width=sample_width,
        )
        result = R.recognize_sphinx(s_audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    except:
        pass
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
        data['item'] = data[2:]
    elif words[0].lower() == 'play':
        data['action'] = 'play'
        data['item'] = data[1:]
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
    return data


def __keyword_check(keyword):
    return keyword.lower() == KEYWORD.lower()


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
    data = {'action': None, 'item': None, 'group': None, 'command': None}
    text = __parse_audio(audio)
    text = 'Hal turn off kitchen lights'
    words = __parse_text_simple(text)
    if len(words) > 0:
        if __keyword_check(words[0]):
            data = __simple_intent(words[1:])
            print('data is')
            print(data)
    return data
