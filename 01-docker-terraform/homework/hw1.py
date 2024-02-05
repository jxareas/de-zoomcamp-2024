#!/usr/bin/env python
# coding: utf-8

# ## Question 1. Knowing docker tags
# 
# Run the command to get information on Docker 
# 
# ```docker --help```
# 
# Now run the command to get help on the "docker build" command:
# 
# ```docker build --help```
# 
# Do the same for "docker run".
# 
# **Which tag has the following text?** - *Automatically remove the container when it exits* 
# 
# - `--delete`
# - `--rc`
# - `--rmc`
# - <font color='red'><b>`--rm`</b></font>

# ## Question 2. Understanding docker first run 
# 
# Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
# Now check the python modules that are installed ( use ```pip list``` ). 
# 
# **What is version of the package *wheel* ?**
# 
# - <font color='red'><b>0.42.0</b></font>
# - 1.0.0
# - 23.0.1
# - 58.1.0

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


# ## Question 3. Count records 
# 
# **How many taxi trips were totally made on September 18th 2019?**
# 
# Tip: started and finished on 2019-09-18. 
# 
# Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.
# 
# - 15767
# - <font color='red'><b>15612</b></font>
# - 15859
# - 89009

# ## Question 4. Longest trip for each day
# 
# **Which was the pick up day with the longest trip distance?**
# Use the pick up time for your calculations.
# 
# Tip: For every trip on a single day, we only care about the trip with the longest distance. 
# 
# Answer: 
# ```postgresql
# SELECT CAST(lpep_pickup_datetime AS DATE), MAX(trip_distance) AS max_trip_distance FROM green_taxi_data
# GROUP BY CAST(lpep_pickup_datetime AS DATE)
# ORDER BY max_trip_distance DESC
# limit 10
# ```
# 
# - 2019-09-18
# - 2019-09-16
# - <font color='red'><b>2019-09-26</b></font>
# - 2019-09-21

# ## Question 5. Three biggest pick up Boroughs
# 
# Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown
# 
# Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
#  
# Answer: 
# ```postgresql
# SELECT z."Borough", ROUND(SUM(total_amount)::numeric, 2) AS total_amount_sum FROM green_taxi_data gtd
# INNER JOIN zones z ON gtd."PULocationID" = z."LocationID"
# WHERE CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
# GROUP BY(z."Borough")
# ORDER BY total_amount_sum DESC
# ```
# 
# - <font color='red'><b>"Brooklyn" "Manhattan" "Queens"</b></font>
# - "Bronx" "Brooklyn" "Manhattan"
# - "Bronx" "Manhattan" "Queens" 
# - "Brooklyn" "Queens" "Staten Island"

# ## Question 6. Largest tip
# 
# For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
# We want the name of the zone, not the id.
# 
# Note: it's not a typo, it's `tip` , not `trip`
# 
# Answer:
# ```postgresql
# select dropoff."Zone", MAX(tip_amount) AS max_tip_amount
# from green_taxi_data gtd
#          inner join zones pickup ON gtd."PULocationID" = pickup."LocationID"
#          inner join zones dropoff on gtd."DOLocationID" = dropoff."LocationID"
# where pickup."Zone" LIKE 'Astoria' AND DATE_TRUNC('month', gtd.lpep_pickup_datetime) = '2019-09-01'::date
# group by dropoff."Zone"
# order by max_tip_amount DESC
# LIMIT 1;
# ```
# 
# - Central Park
# - Jamaica
# - <font color='red'><b>JFK Airport</b></font>
# - Long Island City/Queens Plaza
# 

# ## Terraform
# 
# In this section homework we'll prepare the environment by creating resources in GCP with Terraform.
# 
# In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
# Copy the files from the course repo
# [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.
# 
# Modify the files as necessary to create a GCP Bucket and Big Query Dataset.

# ## Question 7. Creating Resources
# 
# After updating the main.tf and variable.tf files run:
# 
# ```
# terraform apply
# ```
# 
# Paste the output of this command into the homework submission form.
