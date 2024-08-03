from db.mysql_repo import MysqlRepository

def test_load_dict():
    repo = MysqlRepository()
    out = [('book', 'kitaab', 'किताब', 'noun', 'f',
            'physical object consisting of a number of pages bound together'),
           ('tea', 'cāya', 'चाय', 'noun', 'f',
            'a beverage made by steeping tea leaves in water'),
           ('water', 'pānī', 'पानी', 'noun', 'm',
            'a liquid that descends from the clouds as rain, forms streams, lakes, and rivers'),
           ('you', 'tuma', 'तुम', 'pronoun', None,
            'the one being addressed, pronoun of the second person singular')]
    result = repo.load_dictionary()
    assert result == out

def test_load_entry():
    repo = MysqlRepository()
    entry = repo.load_entry('book')
    assert len(entry) > 0

def test_generate_entry():
    repo = MysqlRepository()
    entry = repo.load_entry('book')
    assert entry[0][0] == 'book'
    assert entry[0][1] == 'kitaab'
    assert entry[0][2] == 'किताब'
    assert entry[0][3] == 'noun'
    assert entry[0][4] == 'f'
    assert entry[0][5] == 'physical object consisting of a number of pages bound together'