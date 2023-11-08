
# Hadoop MapReduce on the Cloud

This guide provides step-by-step instructions to run two mapreduce jobs on a managed hadoop cluster using [Google Dataproc](https://cloud.google.com/dataproc?hl=en)  

#### URLs for the Docker Hub images that were used
- [sa-frontend-cloud: Front-end](https://hub.docker.com/r/okemawo1/sa-frontend-cloud) 
- [sa-webapp-cloud: Java back-end](https://hub.docker.com/r/okemawo1/sa-webapp-cloud)
- [sa-logic-cloud: Python back-end](https://hub.docker.com/r/okemawo1/sa-logic-cloud)

#### URLs for the video recordings
- [The application functionality demo on the cloud](https://drive.google.com/file/d/1HuzNS0RCTWZ8e8wyRsG4ntgedPzni69w/view?usp=sharing)
- [Code walkthrough for your code changes](https://drive.google.com/file/d/1TBoXN09Vl85EioJaVPjRcoaFDqC3j1cu/view?usp=sharing)

<br>
<br>

<p align="center">
  <img src="https://github.com/Cloud-Infrastructure-Fall-2023/hw-3-microservice-orchestration-okemawo/assets/65502643/94ec9ea9-a67b-4de3-a15e-a853f7fb9a1f" alt="Deployment Diagram">
</p>
<br>

## Prerequisites

- [Google Cloud Platform (GCP) account](https://console.cloud.google.com/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed
- `kubectl` (Kubernetes command-line tool) installed
- [Docker](https://www.docker.com/get-started) installed
- [nodeJs](https://nodejs.org/en) installed
- [npm](https://www.npmjs.com/) installed
- [maven](https://maven.apache.org/what-is-maven.html) installed
- [jdk](https://www.oracle.com/java/technologies/downloads/) installed


### Clone the Repository

```bash
git clone https://github.com/rinormaloku/k8s-mastery.git
```
<br>

### Login to docker hub 
- You will be promted to input your username and password or access token 
```bash
docker login
```
<br>

### Install Software Tools
- Docker
```bash
apt install docker.io
docker --version
```


# ALL DONE!!!
