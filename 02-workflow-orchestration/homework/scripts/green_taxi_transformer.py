import pandas as pd
import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Passenger count is greater than 0 and the trip distance is greater than zero
    passenger_count_and_trip_distance_greater_than_zero = (data['passenger_count'] > 0) & (data['trip_distance'] > 0)
    data = data[passenger_count_and_trip_distance_greater_than_zero]

    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    data.rename(columns={col: camel_to_snake(col) for col in data.columns}, inplace=True)

    return data


def camel_to_snake(column_name):
    """
    Convert Camel Case to Snake Case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


def test_vendor_id(output, *args) -> None:
    """
    Test if 'vendor_id' values are valid.
    """
    assert 'vendor_id' in output.columns, 'Invalid vendor_id values'


def test_passenger_count(output, *args) -> None:
    """
    Test if 'passenger_count' is greater than 0.
    """
    assert (output['passenger_count'] > 0).all(), 'Passenger count should be greater than 0'


def test_trip_distance(output, *args) -> None:
    """
    Test if 'trip_distance' is greater than 0.
    """
    assert (output['trip_distance'] > 0).all(), 'Trip distance should be greater than 0'
