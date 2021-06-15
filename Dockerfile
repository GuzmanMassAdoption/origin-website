FROM python:3.8.8-slim-buster

# Install requirements
WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

# Install watchdog for auto restart on code changes
RUN pip install pyyaml argh watchdog
