# the starting point image to build your layers on top off 
FROM python:3.5-alpine

COPY app.py boot.sh ./
COPY requirements requirements
# executes commands 
RUN pip install -r requirements/docker.txt
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"] 
