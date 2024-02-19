<br />
<div align="center">
  <a href="#">
    <img src="./assets/dlthub.png" height="150" alt="DLT Logo">
  </a>

<h1 align = "center">
<b><i>dlt</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

**`dlt`** is a python library created for the purpose of assisting data engineers to build simpler, faster and more robust
pipelines with minimal effort.

You can think of dlt as a loading tool that implements the best practices of data pipelines enabling you to just “use”
those best practices in your own pipelines, in a declarative way.

This enables you to stop reinventing the flat tyre, and leverage dlt to build pipelines much faster than if you did
everything from scratch.

dlt automates much of the tedious work a data engineer would do, and does it in a way that is robust. dlt can handle
things like:

- Schema: Inferring and evolving schema, alerting changes, using schemas as data contracts.
- Typing data, flattening structures, renaming columns to fit database standards. In our example we will pass the “data”
  you can see above and see it normalised.
- Processing a stream of events/rows without filling memory. This includes extraction from generators.
- Loading to a variety of dbs or file formats.

Let’s use it to load our nested json to duckdb:

Here’s how you would do that on your local machine. I will walk you through before showing you in colab as well.

First, install dlt

```bash
# Make sure you are using Python 3.8-3.11 and have pip installed
# spin up a venv
python -m venv ./env
source ./env/bin/activate
# pip install
pip install dlt[duckdb]
```

Next, grab your data from above and run this snippet

- here we define a pipeline, which is a connection to a destination
- and we run the pipeline, printing the outcome

```python
# define the connection to load to. 
# We now use duckdb, but you can switch to Bigquery later
pipeline = dlt.pipeline(pipeline_name="taxi_data",
                        destination='duckdb',
                        dataset_name='taxi_rides')

# run the pipeline with default settings, and capture the outcome
info = pipeline.run(data,
                    table_name="users",
                    write_disposition="replace")

# show the outcome
print(info)
```

If you are running dlt locally you can use the built in streamlit app by running the cli command with the pipeline name
we chose above.

```bash
dlt pipeline taxi_data show
```

Or explore the data in the linked colab notebook. I’ll switch to it now to show you the data.

# Incremental loading

Incremental loading means that as we update our datasets with the new data, we would only load the new data, as opposed
to making a full copy of a source’s data all over again and replacing the old version.

By loading incrementally, our pipelines run faster and cheaper.

- Incremental loading goes hand in hand with incremental extraction and state, two concepts which we will not delve into
  during this workshop
  - `State` is information that keeps track of what was loaded, to know what else remains to be loaded. dlt stores the
    state at the destination in a separate table.
  - Incremental extraction refers to only requesting the increment of data that we need, and not more. This is tightly
    connected to the state to determine the exact chunk that needs to be extracted and loaded.
- You can learn more about incremental extraction and state by reading the dlt docs on how to do it.

### dlt currently supports 2 ways of loading incrementally:

1. Append:
  - We can use this for immutable or stateless events (data that doesn’t change), such as taxi rides - For example,
    every day there are new rides, and we could load the new ones only instead of the entire history.
  - We could also use this to load different versions of stateful data, for example for creating a “slowly changing
    dimension” table for auditing changes. For example, if we load a list of cars and their colors every day, and one
    day one car changes color, we need both sets of data to be able to discern that a change happened.
2. Merge:
  - We can use this to update data that changes.
  - For example, a taxi ride could have a payment status, which is originally “booked” but could later be changed into
    “paid”, “rejected” or “cancelled”

Here is how you can think about which method to use:

![Incremental Loading](./incremental_loading.png)

* If you want to keep track of when changes occur in stateful data (slowly changing dimension) then you will need to
  append the data

### Let’s do a merge example together:

> 💡 This is the bread and butter of data engineers pulling data, so follow along.

- In our previous example, the payment status changed from "booked" to “cancelled”. Perhaps Jack likes to fraud taxis
  and that explains his low rating. Besides the ride status change, he also got his rating lowered further.
- The merge operation replaces an old record with a new one based on a key. The key could consist of multiple fields or
  a single unique id. We will use record hash that we created for simplicity. If you do not have a unique key, you could
  create one deterministically out of several fields, such as by concatenating the data and hashing it.
- A merge operation replaces rows, it does not update them. If you want to update only parts of a row, you would have to
  load the new data by appending it and doing a custom transformation to combine the old and new data.

In this example, the score of the 2 drivers got lowered and we need to update the values. We do it by using merge write
disposition, replacing the records identified by  `record hash` present in the new data.

```python
data = [
  {
    "vendor_name": "VTS",
    "record_hash": "b00361a396177a9cb410ff61f20015ad",
    "time": {
      "pickup": "2009-06-14 23:23:00",
      "dropoff": "2009-06-14 23:48:00"
    },
    "Trip_Distance": 17.52,
    "coordinates": {
      "start": {
        "lon": -73.787442,
        "lat": 40.641525
      },
      "end": {
        "lon": -73.980072,
        "lat": 40.742963
      }
    },
    "Rate_Code": None,
    "store_and_forward": None,
    "Payment": {
      "type": "Credit",
      "amt": 20.5,
      "surcharge": 0,
      "mta_tax": None,
      "tip": 9,
      "tolls": 4.15,
      "status": "cancelled"
    },
    "Passenger_Count": 2,
    "passengers": [
      {"name": "John", "rating": 4.4},
      {"name": "Jack", "rating": 3.6}
    ],
    "Stops": [
      {"lon": -73.6, "lat": 40.6},
      {"lon": -73.5, "lat": 40.5}
    ]
  },
]

# define the connection to load to. 
# We now use duckdb, but you can switch to Bigquery later
pipeline = dlt.pipeline(destination='duckdb', dataset_name='taxi_rides')

# run the pipeline with default settings, and capture the outcome
info = pipeline.run(data,
                    table_name="users",
                    write_disposition="merge",
                    merge_key="record_hash")

# show the outcome
print(info)
```

As you can see in your notebook, the payment status and Jack’s rating were updated after running the code.

### What’s next?

- You could change the destination to parquet + local file system or storage bucket. See the colab bonus section.
- You could change the destination to BigQuery. Destination & credential setup
  docs: https://dlthub.com/docs/dlt-ecosystem/destinations/, https://dlthub.com/docs/walkthroughs/add_credentials
  or See the colab bonus section.
- You could use a decorator to convert the generator into a customised dlt
  resource: https://dlthub.com/docs/general-usage/resource
- You can deep dive into building more complex pipelines by following the guides:
  - https://dlthub.com/docs/walkthroughs
  - https://dlthub.com/docs/build-a-pipeline-tutorial
- You can join our [Slack community](https://dlthub.com/community) and engage with us there.
