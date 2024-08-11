from app.services import *
from db.mysql_repo import *

services = Services()
repo = MysqlRepository()

def test_generate_entry():
    service = services.generate_entry('tea')
    entries = repo.load_entry('tea')
    assert len(entries) > 0
    assert len(service) > 0
    assert service == entries


