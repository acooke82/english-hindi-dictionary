from model.word import Word
from model.enums import PartOfSpeech, Gender, Tense

def test_word():
    word = Word(english_form="book")
    assert word.english_form == "book"

def test_word2():
    word = Word(devanagari="kitaab")
    assert word.devanagari == "kitaab"

def test_noun():
    word = Word(pos=PartOfSpeech.noun)
    assert word.pos == PartOfSpeech.noun

def test_gender():
    word = Word(pos=PartOfSpeech.noun)
    assert Gender == Gender

def test_tense():
    word = Word(pos=PartOfSpeech.verb)
    assert Tense == Tense

