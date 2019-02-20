FROM python:alpine3.7

RUN apk add --no-cache bash

ADD ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

ADD ./src /app

EXPOSE 8888

WORKDIR /app

CMD ["bash", "run_gunicorn.sh"]