<br />
<div align="center">
  <a href="#">
    <img src="./assets/orchestration.svg" height="150" alt="Orchestration Logo">
  </a>

<h1 align = "center">
<b><i>Orchestration</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

In the realm of data engineering, orchestrating complex workflows is essential for managing data pipelines efficiently.
Orchestration tools play a pivotal role in coordinating and automating the execution of tasks within these workflows.
Some popular tools in this domain are Apache Airflow, Luigi, Argo, Prefect & Mage.

## Data Engineering Lifecycle

![Data Engineering Lifecycle](assets/data_engineering_lifecycle.png)

A large part of data engineering is extracting, transforming, and loading data between sources.

Orchestration is a process of dependency management, facilitated through automation.

The data orchestrator manages scheduling, triggering, monitoring and even resource allocation.

Every workflow requires sequential steps.

**Steps = tasks**

**Workflows = DAGs/ pipeline**

Orchestration is an undercurrent because it happens throughout the entire process while being a key component of it.

## Qualities

A good orchestrator handles:

- Workflow management
- Automation
- Error handling
- Recovery
- Monitoring and alerting
- Resource optimization
- Observability
- Debugging
- Compliance and auditing
- Developer Experience


<br />
<div align="center">
  <a href="#">
    <img src="./assets/mage.svg" height="200" alt="Mage Logo">
  </a>

<h1 align = "center">
<b><i>Mage</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

Mage is a Workflow Orchestration tool that allows you to build, run, and manage data pipelines for integrating and
transforming data.
It allows you to create real-time and batch pipelines to transform data using several programming languages, such as
Python, SQL and R.

# Core Abstractions

![](assets/mage_capacities.png)

- 🏢  **Project**: Like a repository on GitHub; this is where you write all your code.
- 🪈  **Pipeline**: Contains references to all the blocks of code you want to run, charts for visualizing data, and
  organizes the dependency between each block of code.
- 🧱  **Block**: A file with code that can be executed independently or within a pipeline.
- 🤓  **Data Product**:  Every block produces data after it’s been executed. These are called data products in Mage.
- ⏰  **Trigger**:  A set of instructions that determine when or how a pipeline should run.
- 🏃‍♂️  **Run Stores**: information about when it was started, its status, when it was completed, any runtime variables
  used in the execution of the pipeline or block, etc.

<br />
<div align="center">
  <a href="#">
    <img src="assets/bigquery.png" alt="Google BigQuery Logo"  height="200">
  </a>

<h1 align = "center">
<b><i>Google BigQuery</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

Google BigQuery is Google's serverless data warehouse that enables scalable analysis over petabytes of data.
It consists of a platform as a service which supports querying using a SQL-dialect and has several built-in
machine learning capabilities.

## Advantages

- Serverless. No software installation required.
- Scalability
- High-availability
- Built-in features (machine learning, geospatial analysis, business intelligence)
- Flexibility: separates the compute engine from the storage

## Cost

* On Demand Pricing
  * 1 TB of data processed is 5$
* Flat rate Pricing
  * Based on number of pre-requested slots
  * 100 slots -> 2000$ monthly = 400TB data processed on demand pricing

## Partitioning

Partitioning in BigQuery involves organizing data into smaller, manageable subsets based on a specific column or
expression. This helps improve query performance and reduce costs by enabling efficient data retrieval.

We can partition by:

- Time-unit column
- Ingestion time (`_PARTITIONTIME`)
- Integer range
- When using Time unit or ingestion time
  - Daily (Default)
  - Hourly
  - Monthly or yearly

Number of partitions limit is 4000.

![Big Query Partitioning](assets/bigquery_partitioning.png)

## Clustering

Clustering is another optimization technique in BigQuery that complements partitioning. In BigQuery, clustering helps in
automatically organizing the data based on the clustered column/columns. Clustering is usually performed on columns with
high cardinality and can be done on a partitioned table as well, to get the maximum performance increase of your
queries.

- Columns you specify are used to colocate related data
- Order of the column is important
- The order of the specified columns determines the sort order of the data.
- Clustering improves
  - Filter queries
  - Aggregate queries
- Table with data size < 1 GB, don’t show significant improvement with partitioning and clustering
- You can specify up to four clustering columns

![Big Query Clustering](assets/bigquery_clustering.png)

## Partitioning v Clustering

| Clustering                                                              | Partitioning                         |
|-------------------------------------------------------------------------|--------------------------------------|
| Cost benefit unknown                                                    | Cost known upfront                   |
| You need more granularity than partitioning alone allows                | You need partition-level management  |
| Queries commonly use filters or aggregations against particular columns | Filter or aggregate on single column |
| The cardinality of the number of values in a column is large            | ------------------------------------ |

## Best Practices

### Cost Reduction

* Avoid `SELECT *`, specify columns as needed
* Price your queries before running them
* Use clustered or partitioned tables
* Use streaming inserts with caution
* Materialize query results in stages

### Query Performance

* Filter on partitioned columns
* Denormalize data
* Reduce data before using `JOIN` clauses
* Do not treat `WITH` clauses as prepared statements

## BigQuery Internals

Let’s explore the below illustration of the overall architecture of BigQuery point by point.
First, let's note that storage and compute are separated, which is the cause of BigQuery's outstanding
performance for large-scale data analysis.

- **Dremel**: Query execution engine, which breaks each query into a tree structure, which is executed in parallel
  across various nodes.
- **Colossus**: Google's distributed file storage that stores data in a columnar format, where BigQuery natively stores
  customer data in Google Cloud Platform.
- **Jupiter** A fast network for communication, implemented inside Google's data center and has ~1TB bandwidth.

![img.png](assets/bigquery_architecture.png)
