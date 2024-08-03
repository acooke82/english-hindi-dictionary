from model.enums import *
from model.word import Word


class Verb(Word):

    def __init__(self,
                 tense: Tense):
        self.tense = tense
