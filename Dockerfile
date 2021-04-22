FROM ubuntu:xenial
RUN apt.txt
RUN cat requirements.txt | xargs -n 1 pip install
RUN postBuild.txt
