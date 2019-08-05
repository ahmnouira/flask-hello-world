# flask-hello-world
This is a simple flask application 

# Overview
![hello_ahmed](/img/hello_ahmed.png)

# Running this app

This app is designed to run in different ways:
1. As a standalone app running on your machine
2. As a Docker container running locally 
3. As a Docker image published in Docker Hub

## 1. As a standalone app

1. install [python](https://www.python.org/) 
2. `git clone` the project then `cd` into the directory
3. run `virtualenv -p /usr/bin/python3 venv`or `python -m venv venv` to create a virtual environment
4. activate it using `source venv/bin/activate`
5. `pip install -r requirements.txt` to install the app libaries and it dependencies

### running the app

After installing, run the server using `python app.py`
Access the running app in a browser at the URL written to the console (most likely http://localhost:5000)

## 2. As a Docker container running on your machine

1. install [Docker](https://www.docker.com/)
2. `run docker --version` to check if docker is installed
3. run `docker build -t flask-hello-world:latest .` to build the docker image
4. `docker images` list the local avaible images
5. run `docker run --name flask_hello_world -d -p 8000:5000 --rm flask-hello-world:latest` to start the container
6. Navigate to http://localhost:8000 in a browser to see the results. If you want to share it with your local network devices navigate to http://[your-ip-address]:8000

## 3. As a Docker image published in Docker Hub
Docker Hub is a free service to publicly store available images.
1. you need to install only [Docker](https://www.docker.com/)
2. just run `docker run -d -p 8080:5000 --name flask ahmnouira/flask-hello-world` 
![my_doker_hub](/img/docker_hub.png)

