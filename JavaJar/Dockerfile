# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN apt update
RUN apt install -y make
RUN apt install -y openjdk-8-jdk
RUN make /app
CMD java -cp /app/test-0.0.1-SNAPSHOT.jar com.shaji.utils.App
