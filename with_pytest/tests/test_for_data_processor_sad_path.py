import pytest
from scripts import data_processor


@pytest.fixture(scope="function")
def city_list_location_malformed_path():
    yield 'tests/resources/malformed_map.csv'


def test_csv_render_malformed_data_contents(city_list_location_malformed_path):
    """
    Sad Path Test
    we will need to wrap the follwoing line in the
    exceptions context manager
    """
    with pytest.raises(ValueError) as exp:
        data_processor.csv_reader(city_list_location_malformed_path)
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"
