from model.givenentry import GivenEntry

def test_returnentry():
    test_entry = 'a string'
    ge = GivenEntry(given_entry=test_entry)
    assert ge.return_entry()['given entry'] == test_entry

