# Spark

Apache Spark is an open-source multi-language unified analytics engine for large-scale data processing.
- Spark is an engine because it processes data.
- Spark can be run in clusters with multiple nodes, each pulling and transforming data.
- Spark is multi-language because we can use Java and Scala natively, and there are wrappers for Python, R, and other languages. The wrapper for Python is called PySpark.

Spark can be used to execute both batch and streaming jobs. A streaming job is essentially a sequence of small batch jobs.

### When to use Spark?

Spark is used for processing data in a Data Lake.

![spark workflow](res/spark-workflow.png)

There are tools such as Hive, Presto, or Athena that allow us to express jobs as SQL queries. If a batch job can be expressed with SQL, then these tools should be used.

However, there are times where we need to apply more complex manipulation which is very difficult or even impossible to express with SQL. In these instances, Spark is the tool to use.

## Installation (Windows)

### Install Java

Download **Java** from: [Java](https://www.java.com/en/)
- Spark runs on Java 8/7/11
- Install JRE-8 and change the destination folder to `C:\jre-8`
- Add a new **System Variable**
    - Variable name = `JAVA_HOME`
    - Variable value = `C:\jre-8`
- Check that Java works correctly by running `java -version` in the command prompt
    - We should see version `1.8.0`
- Run the command `echo %JAVA_HOME%` to see the location of Java

### Install Hadoop

- Create a folder `C:\hadoop-3.0.0\bin`
- Download `winutils.exe` and `hadoop.dll` from: [Hadoop Binaries](https://github.com/steveloughran/winutils/blob/master/hadoop-3.0.0/bin/) and save it in the folder
- Add a new **System Variable**
    - Variable name = `HADOOP_HOME`
    - Variable value = `C:\hadoop-3.0.0`
- Edit the **User Variable** `Path`
    - Add a new value `%HADOOP_HOME%\bin`

### Install Spark

- Create a folder `C:\spark`
- Navigate to this folder in Git Bash and download Spark by running: `curl -LfO https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz`
- Untar the file by running `tar xzfv spark-3.3.2-bin-hadoop3.tgz`
- Add a new **System Variable**
    - Variable name = `SPARK_HOME`
    - Variable value = `C:\spark\spark-3.3.2-bin-hadoop3`
- Edit the **User Variable** `Path`
    - Add a new value `%SPARK_HOME%\bin`
- To test the installation, navigate to `spark-3.3.2-bin-hadoop3` directory
    - Run `./bin/spark-shell.cmd`
    - Then run the following code:
    ```scala
    val data = 1 to 10000
    val distData = sc.parallelize(data)
    distData.filter(_ < 10).collect()
    ```

Testing did not work in Git Bash but it did in Command Prompt.

![spark install test](res/spark-install-test.png)

### Install PySpark

- Run `pip install pyspark` or `pipenv install pyspark`

## Spark Basics

We will import `pyspark` in a Jupyter notebook to learn how to use Spark.

### Creating a Spark session

`SparkSession` is an object that is used for interacting with Spark.

```python
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()
