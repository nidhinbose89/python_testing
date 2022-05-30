import pytest

###########################################
# MOVED FIXTURES TO tests/conftest.py  ####
###########################################

def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    data = process_data(file_name_or_type="clean_map.csv")
    header_fields = list(data[0].keys())
    assert header_fields == [
            'Country',
            'City',
            'State_Or_Province',
            'Lat',
            'Long',
            'Altitude'
            ]


def test_csv_reader_data_contents(process_data):
    """
    Happy Path Test to examine that each row
    had the appropriate data type per field
    """
    data = process_data(file_name_or_type="clean_map.csv")

    # Check row types
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))

    # Basic data checks
    assert len(data) == 180  # We have collected 180 rows
    assert data[0]['Country'] == 'Andorra'
    assert data[106]['Country'] == 'Japan'


def test_csv_reader_malformed_data_contents(process_data):
    """
    Sad Path Test
    """
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type="malformed_map.csv")
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"