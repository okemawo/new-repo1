
# Hadoop MapReduce on the Cloud

This guide provides step-by-step instructions and results for running two mapreduce jobs on a managed hadoop cluster using [Google Dataproc](https://cloud.google.com/dataproc?hl=en)  

## Prerequiste
- Create a dataproc cluster using the cloud console 
- Establish a SSH connection with the master node

## Question 1
Here we reate a Hadoop MapReduce application to find the maximum 
temperature in every day of the years 1901 and 1902 from the National Climate 
Data Center weather records. The records exit in two files which represent each year. 

### Finding the Max temperature without a combiner 
- Upload the map, reduce and data files on the local file system of the master node
- Copy the data files from the local file system to HDFS
- Run the Map Reduce Job
- Collect stats

### Finding the max temperature with a combiner 
- Upload the map, combiner, reduce and data files on the local file system of the master node
- Copy the data files from the local file system to HDFS
- Run the Map Reduce Job
- Collect stats

<br>
<br>

## Question 2
Here we develop an efficient algorithm to find the most frequent 10
words using MapReduce fron a collection of text files. Top-N algorithm structure is shown below.

<br>

<p align="center">
<img src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/9570b3eb-b1d6-46f6-b96c-5f23b693b09c">
</p>

<br>

- Create a dataproc cluster using the cloud console 
- Establish a SSH connection with the master node
- Upload the map, combiner, reduce and data files on the local file system of the master node
- Copy the data files from the local file system to HDFS
- Run the Map Reduce Job
- Collect stats

# ALL DONE!!!
