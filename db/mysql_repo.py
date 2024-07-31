import mysql.connector
from db.repository import *


class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run LOCALLY, this should be localhost
            'port': 32000,  # to run LOCALLY, this should be 32000
            'database': 'dictionary'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def load_dictionary(self) -> List[Word]:
        sql = "SELECT * FROM word_info"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
