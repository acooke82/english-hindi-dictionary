from mysql-connector import cursor
import mysql.connector
import db.mysql_repo

repo = db.mysql_repo.MysqlRepository()

def query_db(sql):
    repo.cursor.execute(sql)
    return list(repo.cursor)

def check_columns():
    sql = ("SELECT * FROM word_info")
    result = query_db(sql)
    return result

def test_check_columns():
    result = check_columns()
    assert "english_form" in result