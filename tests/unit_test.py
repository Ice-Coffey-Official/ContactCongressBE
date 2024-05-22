import contentGen
import createDB
from util import *
import pytest

generator = contentGen.ContentGenerator()

def test_database_connections():

    database = createDB.Database()

    assert database.connection == None
    assert database.cursor == None

    with pytest.raises(Exception):
        database.close()

    database.connect()
    database.createCursor()

    assert database.connection != None
    assert database.cursor != None

    database.deleteCursor()
    assert database.cursor == None

    with pytest.raises(Exception):
        database.deleteCursor()

    with pytest.raises(Exception):
        database.connect()

    database.createCursor()
    assert database.cursor != None

    with pytest.raises(Exception):
        database.createCursor()


    
    

