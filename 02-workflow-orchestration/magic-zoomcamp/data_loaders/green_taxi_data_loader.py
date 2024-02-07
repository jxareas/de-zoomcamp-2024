import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Define the URL pattern for the data
    url_pattern = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{}.csv.gz'

    months = [10, 11, 12]

    dfs = []

    green_taxi_data_types = {
        'VendorID': pd.Int64Dtype(),
        'pasangger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RateCodeID': pd.Int64Dtype(),
        'store_and_fwd+flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_mount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    for month in months:
        url = url_pattern.format(month)
        df = pd.read_csv(url, sep=',', compression='gzip', dtype=green_taxi_data_types, parse_dates=parse_dates)
        dfs.append(df)

    # Flatten into a single dataframe
    return pd.concat(dfs, ignore_index=True)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'