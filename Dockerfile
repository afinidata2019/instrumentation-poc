FROM python:3

WORKDIR /srv/service
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY api ./api
