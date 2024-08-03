import db.mysql_repo

class Services:

    def __init__(self):
        self.repo = db.mysql_repo.MysqlRepository()

    def generate_entry(self, input_form: str):
        #use case: take English input as surface form and return all relevant information for that entry from the db
        dictionary = self.repo.load_entry(input_form)
        return dictionary



