from mlproject.distance import haversine
import pytest

def test_haversine():
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 49.3945, 3.3
    distance = haversine(lon1, lat1, lon2, lat2)
    assert distance == 89.14169592868782
