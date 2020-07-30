FROM ubuntu:latest

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*  # remove the cache

COPY requirements.txt /root

RUN python3 -m pip install -r /root/requirements.txt

COPY flatagent /root/flatagent

WORKDIR /root/flatagent

CMD python3 -m flatagent
