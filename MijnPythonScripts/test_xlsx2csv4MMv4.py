import pytest
from xlsx2csv4MMv4 import isValidFileName, exists

def test_isValidFile():
    # positive tests
    assert isValidFileName('Replication_201411.xlsx') is True
    assert isValidFileName('Replication_201412.xlsx') is True
    assert isValidFileName('replication_201411.xlsx') is True

    # negative tests
    with pytest.raises (RuntimeError) as excinfo:
        assert isValidFileName('Replication_2014aa.xlsx')


def test_exists():
    # positive tests
    assert exists('Replication_201411.xlsx') is True

    # negative tests
    with pytest.raises (RuntimeError) as excinfo:
        assert exists('IDoNotExist.xlsx')
