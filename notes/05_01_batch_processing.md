# Overview of Batch Processing

In the realm of data processing, two primary methods are employed: batch processing and streaming data processing. Batch processing involves the analysis of data that has been accumulated over a specific timeframe. This method entails processing data in chunks at regular intervals, such as monthly processing of taxi trip records. On the other hand, streaming data processing occurs in real-time as data flows through a system, allowing for immediate analysis and reporting of events, like processing a taxi trip as soon as it is generated.

## Scheduling and Technologies

Batch jobs are scheduled based on the specific needs of the data processing task. Common schedules include weekly, daily, hourly, or even multiple times per hour, such as every 5 minutes. Various technologies can be employed for batch processing, including Python scripts (compatible with platforms like Kubernetes and AWS Batch), SQL, Spark, and Flink. Workflow orchestration tools, like Airflow, play a crucial role in managing and coordinating these batch jobs.

## Typical Batch Job Workflow

A standard batch job workflow involves a sequence of tasks that are executed in a coordinated manner. This ensures a systematic and efficient execution of data processing. An illustrative example of a batch job workflow is depicted in the diagram below:

![batch jobs workflow](res/batch-jobs-workflow.png)

## Advantages and Disadvantages

### Advantages of Batch Processing

1. **Ease of Management**: Batch jobs benefit from the availability of multiple tools for effective management.
2. **Re-executability**: In the event of failure, jobs can be easily retried, contributing to robust data processing.
3. **Scalability**: Batch processing allows for the execution of scripts on more powerful machines, and technologies like Spark can be deployed in larger clusters.

### Disadvantages of Batch Processing

1. **Delay**: Each task within a batch job workflow may take some time, leading to a cumulative delay in obtaining the final processed data.

Despite the inherent delay, the advantages of batch processing, including manageability, re-executability, and scalability, often outweigh its limitations. Consequently, many data-centric companies prefer utilizing batch jobs for the majority of their data processing needs, accounting for 80-90% of their operations.
