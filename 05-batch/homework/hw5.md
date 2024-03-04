# Homework 3: Batch Processing

**Homework submission link**: [Homework 5 Submission Link](https://courses.datatalks.club/de-zoomcamp-2024/homework/hw5)

**Deadline**: 04 March 2024

## Spark

### Question 1: Install Spark and PySpark

- **Install Spark**
- **Run PySpark**
- **Create a local Spark session**
- **Execute `spark.version`**

**Output**: 3.5.0

### Question 2: FHV October 2019

- **Read the October 2019 FHV** into a Spark Dataframe with a schema as we did in the lessons.
- **Repartition the Dataframe to 6 partitions** and save it to parquet.

**Average size of parquet files (in MB):**
- 1MB
- **6MB**
- 25MB
- 87MB

### Question 3: Count records

**How many taxi trips were there on the 15th of October?**
- 108,164
- 12,856
- 452,470
- **62,610**

### Question 4: Longest trip for each day

**Length of the longest trip in the dataset (in hours):**
- **631,152.50 Hours**
- 243.44 Hours
- 7.68 Hours
- 3.32 Hours

### Question 5: User Interface

**Spark’s User Interface runs on which local port?**
- 80
- 443
- **4040**
- 8080

### Question 6: Least frequent pickup location zone

**Load the [zone lookup data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv) into a temp view in Spark.**

**Using the zone lookup data and the FHV October 2019 data, what is the name of the LEAST frequent pickup location Zone?**
- East Chelsea
- **Jamaica Bay**
- Union Sq
- Crown Heights North
