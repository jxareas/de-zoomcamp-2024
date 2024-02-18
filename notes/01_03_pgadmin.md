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
