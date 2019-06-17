from db_conn import DBConn
import pytest
from unittest.mock import patch

@pytest.fixture
def db_conn(self):
    db_conn = DBConn()
    return(db_conn)

@patch.object(DBConn, 'execute_query')
def test_execute_query(self):
    DBConn.execute_query()





    @patch.object(ManPower, 'appendManPowerSQLTable')
def test_appendManPowerSQLTable(mock_appendDataList):
    ManPower.appendManPowerSQLTable()
    mock_appendDataList.assert_called_once
    
    
    
