from model.enums import *

class Word:
    def __init__(self,
                 english_form: str = None,
                 romanised_hindi: str = None,
                 devanagari: str = None,
                 pos: PartOfSpeech = None,
                 definition: str = None):
        self.english_form = english_form
        self.romanised_hindi = romanised_hindi
        self.devanagari = devanagari
        self.pos = pos
        self.definition = definition

    def assign_gender(pos: PartOfSpeech) -> Gender:
        if pos == PartOfSpeech.noun:
            return Gender

    def assign_tense(pos: PartOfSpeech) -> Tense:
        if pos == PartOfSpeech.verb:
            return Tense
