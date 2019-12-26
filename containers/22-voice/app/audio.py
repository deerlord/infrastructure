import speech_recognition as sr

R = sr.Recognizer()
R.dynamic_energy_threshold = True

def process(audio):
    try:
        sample_rate = int.from_bytes(
            audio[24:48],
            byte_order='little',
        )
        sample_width = 2  # might need to be dynamic
        b_audio = audio[44:]
        s_audio = sr.AudioData(
            b_audio,
            sample_rate=sample_rate,
            sample_width=sample_width,
        )
        result = R.recognize_sphinx(s_audio)
    except:
        result = ''
    return result

