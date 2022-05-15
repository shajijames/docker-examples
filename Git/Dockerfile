# syntax=docker/dockerfile:1
FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
COPY . /app
RUN apt update
RUN apt install -y make
RUN apt install -y python3
RUN apt install -y git-all
RUN make /app
RUN git clone -b main --single-branch https://github.com/shajijames/docker-examples.git /app/FromGit
CMD python3 /app/FromGit/Python/app.py
