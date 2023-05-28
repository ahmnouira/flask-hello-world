# flask-hello-world

This is a simple flask application

## Overview

![hello_ahmed](/img/hello_ahmed.png)

## Running this app

This app is designed to run in different ways:

1. As a standalone app running on your machine
2. As a Docker container running locally
3. As a Docker image published in Docker Hub
4. As an application hosted by [IBM Cloud](https://https://www.ibm.com/cloud)

## 1. As a standalone app

1. install [python](https://www.python.org/)
2. `git clone` the project then `cd` into the directory
3. run `virtualenv -p /usr/bin/python3 venv`or `python -m venv venv` to create a virtual environment
4. activate it using `source venv/bin/activate`
5. `pip install -r requirements.txt` to install the app libraries and it dependencies

### running the app

After installing, run the server using `python app.py`
Access the running app in a browser at the URL written to the console (most likely [http://localhost:5000](http://localhost:50000))

## 2. As a Docker container running on your machine

1. install [Docker](https://www.docker.com/)
2. `run docker --version` to check if docker is installed
3. run `docker build -t flask-hello-world:latest .` to build the docker image
4. `docker images` list the local available images
5. run `docker run --name flask_hello_world -d -p 8000:5000 --rm flask-hello-world:latest` to start the container
6. Navigate to [http://localhost:8000](http://localhost:8000) in a browser to see the results. If you want to share it with your local network devices navigate to *http://[your-ip-address]:8000*

## 3. As a Docker image published in Docker Hub

Docker Hub is a free service to publicly store available images.

1. you need to install only [Docker](https://www.docker.com/)
2. just run `docker run -d -p 8080:5000 --name flask ahmnouira/flask-hello-world`

![my_docker_hub](/img/docker_hub.png)

## 4. As an application hosted by IBM Cloud

 :octocat: Before you begin, verify that you have completed the below steps:

* you have access to an [IBM Cloud account](https://cloud.ibm.com/registration).
* the [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) is installed in your workstation.

1. clone the repository by running  `git clone https://github.com/AhmNouira/flask-hello-world`
2. `cd flask-hello-world`
3. run `bx login` to login to your IBM cloud account and enter your email and password
4. `bx target --cf` to target the Cloud Foundry
To check the default organization and space to which you have access, go to <https://cloud.ibm.com/account/cloud-foundry>.
5. `bx cf push` to push the application to IBM Cloud
6. if you found any error run `bx cf logs flask-hello-world --recent` to see the troubleshoot
7. check whether your app is running `bx cf app flask-hello-world`
8. to explore how your app directories are structured `bx cf ssh flask-hello-world`

![ibm_cloud](/img/ibm_cloud.png)

## 5. Push a new image

Login to the docker.io using the access token

```bash
docker login -u ahmnouira docker.io     
```

Build and tag

```bash
docker build -t flask-hello-world:latest .
```

Tag it as per the docker hub repository name

```bash
docker tag flask-hello-world:latest ahmnouira/flask-hello-world:latest
```

Push the a new image:

```bash
docker image push ahmnouira/flask-hello-world:latest  
```
