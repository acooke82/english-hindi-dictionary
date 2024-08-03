from model.enums import *
from model.word import Word


class Noun(Word):
    def __init__(self,
                 gender: Gender):
        self.gender = gender
