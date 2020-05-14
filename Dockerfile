FROM amazonlinux

COPY pingl.py /home/lab4/pingl.py

COPY multipingl.py /home/lab4/multipingl.py

COPY ping.h /home/lab4/ping.h

COPY ping.cpp /home/lab4/ping.cpp

COPY multiping.cpp /home/lab4/multiping.cpp

COPY input2.txt /home/lab4/input2.txt

RUN yum update -y

RUN yum install -y nano

RUN yum install -y gcc-c++

RUN yum install -y python3

RUN yum install -y nmap

ENTRYPOINT bin/bash