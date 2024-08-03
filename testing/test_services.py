from app.services import *
from db.mysql_repo import *

services = Services()
repo = MysqlRepository()


def test_entry():
    services.load_entry('book')
    entry = repo.load_dictionary()
    assert len(entry) > 0

def test_generate_entry():
    entry = services.load_entry('book')
    assert entry[0][0] == 'book'
    assert entry[0][1] == 'kitaab'
    assert entry[0][2] == 'किताब'
    assert entry[0][3] == 'noun'
    assert entry[0][4] == 'f'
    assert entry[0][5] == 'physical object consisting of a number of pages bound together'
