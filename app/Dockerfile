FROM python:alpine3.8

ADD . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
