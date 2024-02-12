<br />
<div align="center">
  <a href="#">
    <img src="./assets/postgresql.svg" height="200" alt="Postgres Logo">
  </a>

<h1 align = "center">
<b><i>PostgreSQL</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

## What is PostgreSQL?

PostgreSQL, often referred to as Postgres, is a robust open-source RDBMS known for its extensibility, ACID compliance,
and support for complex queries.

## Key Features

- Advanced SQL Support: PostgreSQL supports a wide range of SQL features, including complex queries, indexing, and
  transaction management.
- Extensibility: Users can define custom data types, operators, and functions, making it highly extensible.
- Concurrency Control: Offers Multi-Version Concurrency Control (MVCC) for efficient handling of concurrent
  transactions.
- Scalability: Scales well with large datasets and supports both horizontal and vertical scaling.

## Why Choose PostgreSQL?

### Open Source

Being open-source, PostgreSQL is freely available and supported by a vibrant community, encouraging collaboration and
continuous improvement.

### Extensibility and Customization

Developers can extend PostgreSQL functionalities with custom plugins, data types, and procedural languages.

### Community Support

A large and active community ensures ongoing development, support, and a wealth of resources for troubleshooting and
optimization.

## Setting up PostgreSQL

## Installation

PostgreSQL can be installed on various operating systems. Use package managers like `apt` or `yum` on Linux or download
the installer for Windows and macOS.

## Connecting to PostgreSQL

After installation, connect to the PostgreSQL server using tools like `psql` or graphical interfaces like pgAdmin.

## Setting up Postgres with Docker

To run Postgres we need to use the official Docker image of Postgres.

```yaml
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: [ "CMD", "pg_isready", "-U", "airflow" ]
      interval: 5s
      retries: 5
```

- `image: postgres:13` is the image name:version
- `environment:` environment variables (user, password, database name)
- `volumes` maps a host directory to a container directory. This allows docker to persist state (mounting).

## Running Postgres with Docker

Execute the following command in order to run postgres using docker

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v "./ny-taxi-volume:/var/lib/postgresql/data" \
  -p 5432:5432 \
  postgres:13
```

* `-e POSTGRES_USER="root"`: Sets the Postgres username to "root".
* `-e POSTGRES_PASSWORD="root"`: Sets the password for the Postgres user to "root".
* `-e POSTGRES_DB="ny_taxi"`: Creates a database named "ny_taxi".
* `-v "./ny-taxi-volume:/var/lib/postgresql/data"`: Mounts a volume named "ny-taxi-volume" to persist data in the
  container.
* `-p 5432:5432`: Maps port 5432 on your local machine to port 5432 in the container.
* `postgres:13`: Specifies the Postgres Docker image version 13.
