import db.mysql_repo2
from mysql.connector import cursor

repo = db.mysql_repo2.MysqlRepository()


def query(sql):
    repo.cursor.execute(sql)
    return list(repo.cursor)


def test_query():
    sql = ("SELECT english_form FROM word_info")
    result = query(sql)
    return result[0][0]
