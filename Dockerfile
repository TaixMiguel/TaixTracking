FROM python:3-slim-bullseye

WORKDIR /taixTracking

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN playwright install

COPY . .
CMD python3 /taixTracking/run.py