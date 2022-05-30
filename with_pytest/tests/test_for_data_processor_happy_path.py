import pytest
from scripts import data_processor


@pytest.fixture(scope="function")
def process_data():
    yield data_processor.csv_reader('tests/resources/clean_map.csv')

def test_csv_reader_header_fields(process_data):
    """
        Happy Path test to make sure the
        processed data containes the right header fields
    """
    # helper function imported from conftest.py
    data = process_data
    header_fields = list(data[0].keys())
    assert header_fields == [
        "Country", "City", "State_Or_Province",
        "Lat", "Long", "Altitude"
    ]

def test_csv_reader_data_contetns(process_data):
    """
    Happy Path Test to examine that each row
    has the appropriate data type per field
    """
    data = process_data
    # check row type
    for ro in data:
        assert(isinstance(ro['Country'], str))
        assert(isinstance(ro['Lat'], float))
        assert(isinstance(ro['Long'], float))
        assert(isinstance(ro['Altitude'], float))
    assert len(data) == 180
    # basic data checks