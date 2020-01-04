import json
import sys
from adapt.entity_tagger import EntityTagger
from adapt.tools.text.tokenizer import EnglishTokenizer
from adapt.tools.text.trie import Trie
from adapt.intent import IntentBuilder
from adapt.parser import Parser
from adapt.engine import DomainIntentDeterminationEngine


tokenizer = EnglishTokenizer()
trie = Trie()
tagger = EntityTagger(trie, tokenizer)
parser = Parser(tokenizer, tagger)
engine = DomainIntentDeterminationEngine()

def new_intent(engine, domain, verbs, keywords, **kwargs):
    domain = domain.lower().capitalize()
    engine.register_domain(domain)
    for v in verbs:
        engine.register_entity(v, "Verb", domain=domain)
    for k in keywords:
        engine.register_entity(k, "Keyword", domain=domain)
    intent = IntentBuilder(domain + "Intent")\
        .require("Verb")\
        .optionally("Keyword")
    for key, values in kwargs.items():
        if not isinstance(values, list):
            err = "Called {} with type {} using value {}"
            raise TypeError(err.format(key, type(values), values))
        for v in values:
            engine.register_entity(v, key, domain=domain)
        intent = intent.optionally(key)
    engine.register_intent_parser(intent.build(), domain=domain)


def setup():
    music_verbs = [
        "listen",
        "hear",
        "play",
    ]
    music_keywords = [
        "songs",
        "music",
    ]
    music_genres = [
        "hardocre",
        "punk",
        "r and b",
        "hip hop",
        "rap",
        "classic rock",
    ]
    new_intent(
        engine,
        "music",
        music_verbs,
        music_keywords,
        genres=music_genres
    )


def process(text):
    for intent in engine.determine_intent(text):
        if intent and intent.get('confidence') > 0:
            return intent


setup()
