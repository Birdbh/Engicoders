import pytest

import sys
sys.path.append("src")

from DataGeneration import DataGeneration

def test_create_data_generation():
    data_generation = DataGeneration(1, 5, 1, "2021-01-01 00:00:00")
    assert data_generation.channel_id == 1
    assert data_generation.time_increment == 5
    assert data_generation.field_number == 1
    assert data_generation.start_date == "2021-01-01 00:00:00"
    assert str(data_generation) == "DataGeneration: CHANNEL_ID:1, TIME_INCREMENT:5, FIELD_NUMBER:1, START_DATE:2021-01-01 00:00:00"

def test_setters_and_getters():
    data_generation = DataGeneration(1, 5, 1, "2021-01-01 00:00:00")
    data_generation.set_channel_id(2)
    data_generation.set_time_increment(10)
    data_generation.set_field_number(2)
    data_generation.set_start_date("2021-01-02 00:00:00")
    assert data_generation.get_channel_id() == 2
    assert data_generation.get_time_increment() == 10
    assert data_generation.get_field_number() == 2
    assert data_generation.get_start_date() == "2021-01-02 00:00:00"