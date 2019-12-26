import stanfordnlp

NLP = stanfordnlp.Pipeline(lang='en')

def process(text):
    return NLP(text)
