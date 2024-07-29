from db.repository import *
import mysql.connector

class mysqlrepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run LOCALLY, this should be localhost
            'port': '32000',  # to run LOCALLY, this should be 32000
            'database': 'dictionary'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def mapper(self, entry: dict) -> GivenEntry:
        given_entry = GivenEntry(english_form=entry.get('english_form'))
        return given_entry
    def load_dictionary(self) -> list[GivenEntry]:
        sql = 'SELECT * FROM dictionary'
        self.cursor.execute(sql)
        entries = [{'english_form': english_form, 'romanised_hindi': romanised_hindi,
                    'devanagari': devanagari, 'pos': pos, 'gender': gender, 'definition': definition}
                   for (english_form, romanised_hindi, devanagari, pos, gender, definition) in self.cursor]
        dictionary = [self.mapper(entry) for entry in entries]
        return dictionary
