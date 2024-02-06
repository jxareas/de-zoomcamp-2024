#!/usr/bin/env python
# coding: utf-8

# # Prepare Postgres
#
# Run Postgres and load data as shown in the videos
# We'll use the green taxi trips from September 2019:
#
# ```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```
#
# You will also need the dataset with zones:
#
# ```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```
#
# Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)

# In[16]:


import pandas as pd
from sqlalchemy import create_engine
from time import time

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

engine = create_engine('postgresql://root:root@localhost:5431/ny_taxi')

df_iter = pd.read_csv(url, iterator=True, chunksize=100_000)

while True:

    try:
        t_start = time()

        df = next(df_iter)

        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
        df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

        df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

        t_end = time()

        print('Inserted another chunk, took %.3f second' % (t_end - t_start))

    except StopIteration:
        print("Finished ingesting data into the postgres database")
        break
