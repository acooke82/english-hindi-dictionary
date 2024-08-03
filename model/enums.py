from enum import Enum
class Gender(Enum):
#m is for masculine, f is for feminine, n is for neuter
    m = 1
    f = 2
    n = 3

class PartOfSpeech(Enum):
    noun = 1
    adjective = 2
    pronoun = 3
    verb = 4
    adverb = 5
    preposition = 6
    conjunction = 7
    article = 8
    interjection = 9

class Tense(Enum):
    present = 1
    past = 2
    future = 3