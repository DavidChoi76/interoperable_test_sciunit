FROM ubuntu:xenial
RUN apt-get update
RUN apt apt.txt
RUN cat requirements.txt | xargs -n 1 pip install
RUN postBuild.txt
