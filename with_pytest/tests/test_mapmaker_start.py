import pytest
from scripts.mapmaker_start import Point

def test_make_one_point():
    p1 = Point("Singapore", 1.3521, 103.8198)
    assert p1.get_lat_long() == (1.3521, 103.8198)


def test_invalid_point_generation():
    with pytest.raises(Exception) as e:
        Point("Trivandrum", 8.5241, -182.9366)
    assert str(e.value) == "Invalid lat/long value."

    with pytest.raises(Exception) as e:
        Point(123, 22.22, 33.33)
    assert str(e.value) == "City name has to be a string."
    