 # Running postgres in Docker
 docker run -it -e POSTGRES_USER="root"
  -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi"
   -v C:/Projects/Python/de-zoomcamp-2024/01-docker-terraform/ny_taxi_postgres_data:/var/lib/postgresql/data
   -p 5431:5432
   --name postgres13
   postgres:13

# Connecting to database with pgcli
pgcli -h localhost -p 5431 -u root -d ny_taxi

# Running pgadmin in Docker
docker run -it
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com"
-e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 dpage/pgadmin4

# Executing the ingest data python script
python ingest_data.py --user=root --password=root --host=localhost --port=5431 --database=ny_taxi --table=yellow_taxi_data --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz

# Creating a docker container with from the Ingest Data Docker image
docker run -it --network pg-network taxi_ingest:v001 --user=root --password=root --host=postgres13 --port=5431 --database=ny_taxi --table=yellow_taxi_data --url=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz


