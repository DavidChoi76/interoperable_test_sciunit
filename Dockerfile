FROM ubuntu:xenial
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip
RUN cat requirements.txt | xargs -n 1 pip install
