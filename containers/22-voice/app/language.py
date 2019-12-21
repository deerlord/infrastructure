from io import BytesIO
import speech_recognition as sr
import stanfordnlp

NLP = stanfordnlp.Pipeline(lang='en')
KEYWORD = 'Hal'
R = sr.Recognizer()
R.dynamic_energy_threshold = True

def __keyword_check(k):
    """
    Check if the keyword we found is the right one. 
    """
    return True if k == KEYWORD else False


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


def __parse_text(text):
    words = NLP(text)
    # probably need some processing/handling here
    return words


def __parse_intent(words):
    pass


def pipeline(audio):
    data = {
        'action': None,
        'item': None,
        'group': None,
        'command': None,
        'error': None,
    }
    text = __parse_audio(audio)
    # test text for now
    text = 'Hal turn off kitchen lights'
    words = __parse_text(text)
    if len(words) > 0:
        if __keyword_check(words[0].text):
            data = __parse_intent(words[1:])
    return data

