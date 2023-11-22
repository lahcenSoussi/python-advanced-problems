import pytest
from average_race_time import *

def test_get_data():
    getData = get_data()
    with open(file_name, 'rt') as file:
        content = file.readlines()
    assert getData==content

def test_get_rhines_times():
    getRhinesTimes=get_rhines_times()
    data = ['32:32.006', '33:04', '33:21', '33:25', '33:30', '33:31']
    assert data == getRhinesTimes

def test_average_race_time():
    result = get_average()
    expected = '33:13.834'
    assert result == expected