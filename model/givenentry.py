from model.enums import *

class GivenEntry:
    def __init__(self, given_entry):
        self.given_entry = given_entry

    def return_entry(self) -> dict:
        field = {'given entry': self.given_entry}
        return field

