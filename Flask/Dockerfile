# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN apt update
RUN apt install -y make
RUN apt install -y python3
RUN apt install -y python3-pip
RUN make /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
