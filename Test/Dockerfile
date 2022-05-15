# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN apt update && apt install -y make
RUN apt update && apt install -y python
RUN make /app
CMD python /app/app.py
