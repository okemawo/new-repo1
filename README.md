
# Hadoop MapReduce on the Cloud

This guide provides step-by-step instructions and results for running two mapreduce jobs on a managed hadoop cluster using [Google Dataproc](https://cloud.google.com/dataproc?hl=en)  

## Prerequiste
- Create a dataproc cluster using the cloud console
<p align="center">
<img width="766" height="500" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/19cb09d8-fdee-4ca3-a2cc-c280c30881d5">
</p>

<br>
<br>

- Establish a SSH connection with the master node by clicking on the cluster and selecting the "vm instances" tab to expose the nodes

<p align="center">
<img width="766" height="500" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/9fff776e-90b6-4ae0-850b-b9476921b70d">
</p>

<br>

## Question 1
Here we reate a Hadoop MapReduce application to find the maximum 
temperature in every day of the years 1901 and 1902 from the National Climate 
Data Center weather records. The records exit in two files which represent each year.

### Finding the Max temperature without a combiner 
- Upload the map, reduce and data files on the local file system of the master node
<p align="center">
<img width="678" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/619a3f93-3aa9-48db-bf47-1e70937ed80d">
</p>

- Copy the data files from the local file system to HDFS
<p align="center">
<img width="848" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/96a3a047-512d-4354-b5fe-b3ea4aa571aa">
</p>

- Run the Map Reduce job using the following command
```bash
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file temperature_mapper.py \
-mapper 'python temperature_mapper.py' \
-file temperature_reducer.py \
-reducer 'python temperature_reducer.py' \
-input ./data \
-output /OutputFolder
```
<p align="center">
<img width="848" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/2b0f356d-d89d-4a5b-99b9-f2a43a25f34c">
</p>

- Collect stats after running the job and check the output folder
<p align="center">
<img width="641" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/f1571445-c726-4a6b-98b9-225b18027b28">
</p>

- Merge the result into a single output file
```bash
hadoop fs -getmerge /OutputFolder/ output.txt
```
<br>

<br>

### Finding the max temperature with a combiner 
- Upload the map, combiner, reduce and data files on the local file system of the master node
<p align="center">
<img width="678" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/c36e5a02-1c81-4f7e-951d-bb01053cfbf8">
</p>
- Copy the data files from the local file system to HDFS
<p align="center">
<img width="672" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/b94820a0-dcff-43a1-8740-01b91c10fd59">
</p>

- Run the Map Reduce Job with the combiner using the follwing command
```bash
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file temperature_mapper.py \
-mapper 'python temperature_mapper.py' \
-file temperature_reducer.py \
-reducer 'python temperature_reducer.py' \
-file temperature_combiner.py \
-combiner 'python temperature_combiner.py' \
-input ./data/ \
-output /OutputFolder
```
<p align="center">
<img width="719" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/7252a785-9192-468e-adb0-8704dcc24bdf">
</p>

- Collect stats after running the job and check the output folder
<br>
<p align="center">
<img width="701" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/656a9763-ea92-4bf6-a956-263350c69246">
</p>
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

- Upload the map, combiner, reduce and data files on the local file system of the master node
<p align="center">
<img width="722" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/72bf635b-8c94-43c4-ab1f-ec79879599a8">
</p>

- Copy the data files from the local file system to HDFS
<p align="center">
<img width="718" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/e789160f-2c5c-4a52-a4da-d5ae3df149b2">
</p>

- Run the Map Reduce Job using the following command with only one reducer
```bash
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file top_n_mapper.py \
-mapper 'python top_n_mapper.py' \
-file top_n_reducer.py \
-reducer 'python top_n_reducer.py' \
-input ./data/ \
-output /OutputFolder
-numReduceTasks 1
```
<p align="center">
<img width="716" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/e1b1fe2f-69ce-4248-84b0-6547f7ffd1e7">
</p>

- Collect stats
<p align="center">
<img width="710" alt="image" src="https://github.com/Cloud-Infrastructure-Fall-2023/homework-6-hadoop-mapreduce-on-the-cloud-okemawo/assets/65502643/bbe6496b-6c78-4f26-9665-181a72feb717">
</p>

<br>

- Get the results
```bash
hadoop fs -get /OutputFolder/ output.txt
```
<br>

<br>

# ALL DONE!!!
