FROM ubuntu:latest

ARG TARGETPLATFORM

RUN apt-get update
RUN apt-get install -y python3 python3-pip

WORKDIR /taixTracking
COPY resources resources
RUN bash -e resources/temp/docker/install_chromium.sh ${TARGETPLATFORM}

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# COPY resources resources
RUN rm -rf /taixTracking/resources/temp
COPY src src
COPY run.py run.py

CMD python3 /taixTracking/run.py