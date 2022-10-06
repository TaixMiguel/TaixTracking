FROM python:3.9

ARG TARGETPLATFORM
RUN apt-get install -y python3 pip3

WORKDIR /taixTracking
COPY resources/temp/docker/install_chromium.sh /taixTracking
RUN bash -e install_chromium.sh ${TARGETPLATFORM}

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY resources resources
RUN rm -rf /taixTracking/resources/temp
COPY src src
COPY run.py run.py

CMD python3 /taixTracking/run.py