<br />
<div align="center">
  <a href="#">
    <img src="./assets/postgresql.svg" height="200" alt="Postgres Logo">
  </a>

<h1 align = "center">
<b><i>pgAdmin</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

PGAdmin is a popular open-source administration and management tool for PostgreSQL databases. It provides a
user-friendly interface to interact with your PostgreSQL databases and perform various administrative tasks.

## Key Features

1. **Database Management:**

- Create, modify, and delete databases.
- Manage database schemas and tables.

2. **Query Tool:**

- Execute SQL queries with syntax highlighting and autocompletion.

3. **Server Configuration:**

- Configure PostgreSQL server settings.

4. **User and Role Management:**

- Manage users, roles, and permissions.

5. **Backup and Restore:**

- Easily backup and restore databases.

## Getting Started

To get started with PGAdmin, follow these steps:

1. **Installation:**

- Download and install PGAdmin from the official website [link](https://www.pgadmin.org/).

2. **Connection Setup:**

- Launch PGAdmin and set up connections to your PostgreSQL servers.

3. **Exploring the Interface:**

- Familiarize yourself with the main features such as the Object Browser, Query Tool, and Dashboard.

## Install pgAdmin with Docker

To install pgAdmin with Docker, follow these steps:

1. **Pull the pgAdmin Docker Image:**
   ```bash
   docker pull dpage/pgadmin4
   ```

## Running pgAdmin with Docker

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
```

## Running Postgres and pgAdmin together

In order to run postgres with pgAdmin, we have to create a docker network by running the following
command:

```bash
docker network create pg-network
```

After that, run postgres:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v c:/projects/python/de-zoomcamp-2024/01-docker-terraform/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
```

And finally, run pgAdmin:

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin- \
  dpage/pgadmin4
```

Notice, the Docker network (`pg-network`) serves as a communication bridge between the pgAdmin container and any other
containers or services that may be part of the same network (such as postgres).
By creating a dedicated Docker network for pgAdmin & postgres, you establish an isolated environment where both
containers can communicate with each other using their container names as hostnames. 

<br />
<div align="center">
  <a href="#">
    <img src="./assets/sql.svg" height="150" alt="SQL Logo">
  </a>

<h1 align = "center">
<b><i>SQL Refresher</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

SQL, or Structured Query Language, is a powerful and standardized language used for managing and manipulating
relational databases. It provides a set of commands for performing various operations on database systems, such as
querying, updating, inserting, and deleting data.

## Queries

### Implicit Join

This query demonstrates an implicit join, where data is retrieved from the `yellow_taxi_data` table along with
information about pickup and dropoff locations obtained from the zones table. The `WHERE` clause specifies the
conditions
for matching rows between the tables based on location IDs.

```postgresql
SELECT tpep_pickup_datetime,
       tpep_dropoff_datetime,
       total_amount,
       CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_location"
FROM yellow_taxi_data t,
     zones zpu,
     zones zdo
WHERE t."PULocationID" = zpu."LocationID"
  AND t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

### Inner Join

This query uses explicit inner joins to achieve the same result as the implicit join in the first query.
The `INNER JOIN`
keyword explicitly indicates the relationship between the `yellow_taxi_data` table and the zones table based on
pickup and dropoff location IDs.

```postgresql
SELECT tpep_pickup_datetime,
       tpep_dropoff_datetime,
       total_amount,
       CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_location"
FROM yellow_taxi_data t
       JOIN zones zpu ON t."PULocationID" = zpu."LocationID"
       JOIN zones zdo ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

### Nesting

Nesting in SQL refers to the use of subqueries, where one query is embedded within another. In the example using
PostgreSQL, the main query selects all columns from a table named `yellow_taxi_data` (aliased as `t`), filtering the
results
based on a condition involving a subquery. The subquery selects the `LocationID` column from a table named zones. The
main query retrieves rows from yellow_taxi_data where the `PULocationID` is not found in the result set of the subquery,
and it limits the output to 100 rows.

```postgresql
SELECT *
FROM yellow_taxi_data t
WHERE "PULocationID" NOT IN (SELECT "LocationID" FROM zones)
LIMIT 100;
```

### Grouping

Grouping in SQL is a technique where rows with similar values in one or more columns are grouped together, and aggregate
functions are applied to each group. In this example using PostgreSQL, the query groups taxi trips from the
`yellow_taxi_data` table by the date of drop-off (`tpep_dropoff_datetime`). The `COUNT` function is then applied to each
group
to calculate the number of trips on each day. The results are ordered by the trip count in descending order and limited
to the top 10 days.

```postgresql
SELECT CAST(tpep_dropoff_datetime AS DATE) AS "day",
       COUNT(1)                            AS "trips_count"
FROM yellow_taxi_data t
GROUP BY CAST(tpep_dropoff_datetime AS DATE)
ORDER BY trips_count DESC
LIMIT 10;
```
