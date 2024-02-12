<br />
<div align="center">
  <a href="#">
    <img src="assets/data_ingesting.png" height="200" alt="Postgres Logo">
  </a>

<h1 align = "center">
<b><i>Data Ingesting</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

Data ingestion is a fundamental process in the field of data engineering, playing a crucial role in collecting and
importing data from various sources into a storage or processing system.
This initial step is essential for enabling organizations to harness the power of their data for analysis, reporting,
and decision-making.

## Key Components

1. **Data Sources:**

- Data can originate from diverse sources such as databases, log files, APIs, streaming platforms, and more.
  Understanding the nature and structure of these sources is crucial for effective data ingestion.

2. **Data Formats:**

- Data may exist in various formats, including structured (e.g., relational databases), semi-structured (e.g., JSON,
  XML), and unstructured (e.g., text, images). Data engineers must account for these formats during the ingestion
  process.

3. **Data Integration Tools:**

- Various tools and frameworks are available for data ingestion, such as Apache Kafka, Apache NiFi, and AWS Glue.
  These tools automate and streamline the movement of data, providing scalability, reliability, and monitoring
  capabilities.

4. **Data Transformation:**

- In some cases, data needs to be transformed during the ingestion process to ensure compatibility with the
  destination system. This may involve cleaning, enriching, or aggregating the data.

5. **Data Loading:**

- Once the data is prepared, it is loaded into the target storage or processing system. This could be a data
  warehouse, a data lake, or a real-time analytics platform.

## Running Python Scripts

We can run the [`ingest_data.py`](../01-docker-terraform/ingest_data.py) in order to load the _yellow_taxi_trip_
data to our postgres database engine.

```bash
URL="<https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz>"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url="${URL}"
```

**NOTE:**

- This is not a dangerous way to pass the `password` parameter, as it is hardcoded into the command.
- It is required for us to have `wget` installed in the host machine (particularly on Windows)

Now, when refreshing the database, we can check for the total record count to see if whether the script was successful
or not.
