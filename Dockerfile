FROM ubuntu:latest

RUN apt-get install -y chromium-codecs-ffmpeg
RUN apt-get install -y chromium-codecs-ffmpeg-extra
RUN apt-get install -y chromium-browser
RUN apt-get install -y ./chromium-chromedriver_${ARCH}.deb
RUN apt-get install -y python3 pip3

WORKDIR /taixTracking

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY resources resources
RUN rm -rf /taixTracking/resources/temp
COPY src src
COPY run.py run.py

CMD python3 /taixTracking/run.py