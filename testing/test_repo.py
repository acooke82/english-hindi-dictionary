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
