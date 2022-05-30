import os
import pytest

from scripts import data_processor

"""
### TO IMPORT METHODS TO BE IN CONFTEST
pytest_plugins = [
    "tests.folder_name.file_name_1",
    "tests.folder_name.file_name_2",
]
"""

@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type):
        for f in files:
            if file_name_or_type in f:
                if file_name_or_type != '.json':
                    data = data_processor.csv_reader(city_list_location + f)
                else:
                    data = data_processor.json_reader(city_list_location + f)
        return data

    yield _specify_type