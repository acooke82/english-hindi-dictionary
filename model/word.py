from model.enums import *
from model.givenentry import *

class Word:
    def __init__(self, given_entry, other_language_form, definition, pos):
        self.given_entry = given_entry
        self.other_language_form = other_language_form
        self.definition = definition
        self.pos = pos

    def get_word_info(self):
        fields = {'given_entry': self.given_entry,
                  'other langauge equivalent': self.other_language_form,
                  'definition': self.definition,
                  'part of speech': self.pos}
        return fields

