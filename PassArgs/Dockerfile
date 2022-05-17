# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN apt update
RUN apt install -y make
RUN apt install -y openjdk-8-jdk
RUN apt install -y maven
RUN make /app
WORKDIR /app/test
RUN mvn install
ENTRYPOINT ["java", "-cp", "target/test-0.0.1-SNAPSHOT.jar", "com.shaji.utils.App"]

