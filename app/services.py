from typing import List
import db.mysql_repo
from model.word import Word

class Services:

    def __init__(self):
        self.repo = db.mysql_repo.MysqlRepository()

    def load_entry(self, input_form: str) -> List[Word]:
        dictionary = self.repo.load_dictionary()
        return dictionary


