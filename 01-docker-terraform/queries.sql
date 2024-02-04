-- IMPLICIT JOIN
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

-- INNER JOIN
SELECT tpep_pickup_datetime,
       tpep_dropoff_datetime,
       total_amount,
       CONCAT(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       CONCAT(zdo."Borough", ' / ', zdo."Zone") AS "dropoff_location"
FROM yellow_taxi_data t
         JOIN zones zpu ON t."PULocationID" = zpu."LocationID"
         JOIN zones zdo ON t."DOLocationID" = zdo."LocationID"
LIMIT 100;

-- NESTED QUERIES
-- Checking whether there is a PICKUP location in yellow_taxi_data not included in the zones lookup table
SELECT *
FROM yellow_taxi_data t
WHERE "PULocationID" NOT IN (SELECT "LocationID" FROM zones)
LIMIT 100;

-- NESTED QUERIES
-- Checking whether there is a DROPOFF location in yellow_taxi_data not included in the zones lookup table
SELECT *
FROM yellow_taxi_data t
WHERE "DOLocationID" NOT IN (SELECT "LocationID" FROM zones)
LIMIT 100;

-- GROUP BY: Number of trips per day
SELECT CAST(tpep_dropoff_datetime AS DATE) AS "day",
       COUNT(1) AS "trips_count"
FROM yellow_taxi_data t
GROUP BY CAST(tpep_dropoff_datetime AS DATE)
ORDER BY trips_count DESC
LIMIT 10;
